export default function ProductSpecs({ product }) {
  return (
    <div className="card">
      <h3>Specifications</h3>
      <p><strong>Brand:</strong> {product.brand}</p>
      <p><strong>Model:</strong> {product.model}</p>
      <p><strong>Specs:</strong> {product.specs}</p>
      <p><strong>Price:</strong> KES {product.price}</p>
      <p><strong>Stock:</strong> {product.stock}</p>
    </div>
  );
}
