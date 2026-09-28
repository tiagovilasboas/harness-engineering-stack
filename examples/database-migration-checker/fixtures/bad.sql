-- Bad migration: three blocking findings, no confirmation.
ALTER TABLE orders
  ADD COLUMN loyalty_level INT NOT NULL;

CREATE INDEX idx_orders_loyalty ON orders (loyalty_level);

DROP TABLE legacy_coupons;
