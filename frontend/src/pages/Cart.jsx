import { useState } from "react";
import CartItem from "../components/CartItem";
import { useCart } from "../context/CartContext";
import { createOrder } from "../api/api";

export default function Cart(){
  const { cart, removeFromCart, updateQuantity, clearCart, total } = useCart();
  const [placing, setPlacing] = useState(false);

  const handlePlaceOrder = async () => {
    if (cart.length === 0) {
      alert("Cart is empty");
      return;
    }

    setPlacing(true);
    try {
      // Backend expects one order per record; we loop
      for (const item of cart) {
        const payload = {
          customer_name: "Guest", // replace with real user later
          product_id: item.id,
          quantity: item.quantity
        };
        await createOrder(payload);
      }
      alert("Order placed successfully");
      clearCart();
    } catch (err) {
      console.error(err);
      alert("Failed to place order");
    } finally {
      setPlacing(false);
    }
  };

  return (
    <div className="container">
      <h2>Your Cart</h2>
      {cart.length === 0 && <p>Your cart is empty.</p>}
      <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
        {cart.map(item => (
          <CartItem key={item.id} item={item}
            onRemove={removeFromCart}
            onUpdate={updateQuantity}
          />
        ))}
      </div>

      <div style={{ marginTop: 16 }}>
        <p><strong>Total:</strong> KES {total}</p>
        <button className="button" onClick={handlePlaceOrder} disabled={placing}>
          {placing ? "Placing..." : "Place Order"}
        </button>
      </div>
    </div>
  );
}
