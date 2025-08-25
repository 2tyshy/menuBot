import Link from 'next/link';

export default function Home() {
  return (
    <div>
      <h1>Welcome to menuBot</h1>
      <nav>
        <Link href="/menu">Menu</Link>
        <Link href="/cart">Cart</Link>
        <Link href="/checkout">Checkout</Link>
        <Link href="/contact">Contact</Link>
      </nav>
    </div>
  );
}

