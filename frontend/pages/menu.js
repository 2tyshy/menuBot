import { useEffect, useState } from 'react';
import axios from 'axios';
import useCart from '../hooks/useCart';
import styles from '../styles/Menu.module.css';
import RotatingCard from '../components/RotatingCard';

export default function Menu() {
  const [menu, setMenu] = useState({});
  const { add } = useCart();

  useEffect(() => {
    axios.get('/api/menu').then((res) => setMenu(res.data));
  }, []);

  return (
    <div>
      <h1>Menu</h1>
      {Object.entries(menu).map(([cat, items]) => (
        <div key={cat}>
          <h2>{cat}</h2>
          <div className={styles.grid}>
            {items.map((item) => (
              <div key={item.sku} className={styles.card}>
                <RotatingCard image={item.photo} />
                <h3>{item.title}</h3>
                <p>{item.desc}</p>
                <p>{item.price} VND</p>
                <button onClick={() => add(item.sku)}>Add to cart</button>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}

