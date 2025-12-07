import { useEffect, useState } from "react";
import { fetchOrders } from "../api/api";

export default function Orders(){
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    fetchOrders().then(setOrders).catch(err => console.error(err));
  }, []);

  return (
    <div className="container">
      <h2>Orders</h2>
      {orders.length === 0 && <p>No orders found.</p>}
      <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
        {orders.map(o => (
          <div key={o.id} className="card">
            <h4>Order #{o.id}</h4>
            <p className="small">Customer: {o.customer_name || "Guest"}</p>
            <p><strong>Status:</strong> {o.status}</p>
            <p><strong>Product ID:</strong> {o.product_id}</p>
            <p><strong>Quantity:</strong> {o.quantity}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
