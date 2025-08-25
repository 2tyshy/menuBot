import { useEffect, useState } from 'react';
import axios from 'axios';
import useCart from '../hooks/useCart';

export default function Cart() {
  const { cart, remove, clear } = useCart();
  const [items, setItems] = useState([]);

  useEffect(() => {
    axios.get('/api/menu').then((res) => {
      const all = Object.values(res.data).flat();
      const mapped = Object.entries(cart).map(([sku, qty]) => {
        const data = all.find((i) => i.sku === sku);
        return { ...data, qty };
      });
      setItems(mapped);
    });
  }, [cart]);

  const total = items.reduce((s, it) => s + it.price * it.qty, 0);

  return (
    <div>
      <h1>Cart</h1>
      {items.map((item) => (
        <div key={item.sku}>
          {item.title} x{item.qty} - {item.price * item.qty} VND
          <button onClick={() => remove(item.sku)}>Remove</button>
        </div>
      ))}
      <p>Total: {total} VND</p>
      <button onClick={clear}>Clear</button>
    </div>
  );
}

