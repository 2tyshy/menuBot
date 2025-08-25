import { useState } from 'react';
import axios from 'axios';
import useCart from '../hooks/useCart';

export default function Checkout() {
  const { clear } = useCart();
  const [form, setForm] = useState({ address: '', name: '', phone: '', method: 'cash' });
  const [result, setResult] = useState(null);

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const submit = async () => {
    await axios.post('/api/delivery', {
      address: form.address,
      name: form.name,
      phone: form.phone,
    });
    const res = await axios.post('/api/payment', { method: form.method });
    clear();
    setResult(res.data.order);
  };

  if (result) {
    return (
      <div>
        <h1>Order confirmed</h1>
        <p>Transaction: {result.payment.transaction_id}</p>
      </div>
    );
  }

  return (
    <div>
      <h1>Checkout</h1>
      <input name="address" placeholder="Address" value={form.address} onChange={handleChange} />
      <input name="name" placeholder="Name" value={form.name} onChange={handleChange} />
      <input name="phone" placeholder="Phone" value={form.phone} onChange={handleChange} />
      <select name="method" value={form.method} onChange={handleChange}>
        <option value="cash">Cash</option>
        <option value="online">Online</option>
      </select>
      <button onClick={submit}>Pay</button>
    </div>
  );
}

