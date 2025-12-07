import { useState, useEffect } from "react";
import axios from "axios";

export default function Orders({ isAdmin = false }) {
  const [orders, setOrders] = useState([]);
  const [email, setEmail] = useState(""); // user email filter for normal users

  const fetchOrders = async () => {
    try {
      let url = "http://127.0.0.1:8000/orders/";
      const params = {};

      if (!isAdmin) {
        // normal users only see their own orders
        if (!email) return; // require email input
        params.customer_email = email;
      }

      const response = await axios.get(url, { params });
      setOrders(response.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchOrders();
  }, [email, isAdmin]);

  return (
    <div>
      <h2>Orders</h2>

      {!isAdmin && (
        <div style={{ marginBottom: 16 }}>
          <input
            type="email"
            placeholder="Enter your email to view your orders"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
      )}

      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th>Order ID</th>
            <th>Product ID</th>
            <th>Quantity</th>
            <th>Customer</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((order) => (
            <tr key={order.id}>
              <td>{order.id}</td>
              <td>{order.product_id}</td>
              <td>{order.quantity}</td>
              <td>{order.customer_name}</td>
              <td>{order.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
