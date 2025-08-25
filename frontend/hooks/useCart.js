import { useState, useEffect } from 'react';

// Simple cart hook that persists state in localStorage
export default function useCart() {
  const [cart, setCart] = useState({});

  useEffect(() => {
    const stored = localStorage.getItem('cart');
    if (stored) {
      setCart(JSON.parse(stored));
    }
  }, []);

  useEffect(() => {
    localStorage.setItem('cart', JSON.stringify(cart));
  }, [cart]);

  const add = (sku) => {
    setCart((prev) => ({ ...prev, [sku]: (prev[sku] || 0) + 1 }));
  };

  const remove = (sku) => {
    setCart((prev) => {
      const next = { ...prev };
      delete next[sku];
      return next;
    });
  };

  const clear = () => setCart({});

  return { cart, add, remove, clear };
}

