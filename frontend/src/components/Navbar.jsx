import { Link } from "react-router-dom";
import { useCart } from "../context/CartContext";

export default function Navbar(){
  const { cart } = useCart();
  const itemCount = cart.reduce((s, i) => s + i.quantity, 0);

  return (
    <header className="navbar">
      <div style={{display:"flex",gap:12,alignItems:"center"}}>
        <Link to="/"><strong>TeknoDuka</strong></Link>
        <Link to="/categories" style={{color:"#d1d5db"}}>Categories</Link>
        <Link to="/products" style={{color:"#d1d5db"}}>Products</Link>
        <Link to="/orders" style={{color:"#d1d5db"}}>Orders</Link>
      </div>

      <div>
        <Link to="/cart" style={{color:"white"}}>Cart ({itemCount})</Link>
      </div>
    </header>
  );
}
