-- Good migration: backfill-safe column, concurrent index, lock timeout set.
SET lock_timeout = '5s';

ALTER TABLE orders
  ADD COLUMN coupon_code TEXT DEFAULT '';

CREATE INDEX CONCURRENTLY idx_orders_coupon ON orders (coupon_code);
