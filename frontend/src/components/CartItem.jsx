export default function CartItem({ item, onRemove, onUpdate }) {
  return (
    <div className="card" style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
      <div>
        <h4>{item.name || `${item.brand || ""} ${item.model || ""}`}</h4>
        <p className="small">KES {item.price} • Qty: 
          <input
            type="number"
            min="1"
            value={item.quantity}
            onChange={(e) => onUpdate(item.id, Number(e.target.value))}
            style={{ width: 60, marginLeft: 8 }}
          />
        </p>
      </div>
      <div>
        <button className="button" onClick={() => onRemove(item.id)}>Remove</button>
      </div>
    </div>
  );
}
