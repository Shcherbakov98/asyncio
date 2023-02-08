-- create database if not exist
SELECT 'CREATE DATABASE warehouse' WHERE NOT EXISTS (SELECT FROM pg_database where datname = 'warehouse')\gexec

-- connect to database
\connect warehouse;

-- change max_connections for async
ALTER SYSTEM SET max_connections = 500;

-- create superuser and grant all privileges if not exist
DO
$do$
    BEGIN
        IF NOT EXISTS(
                SELECT FROM pg_catalog.pg_roles
                WHERE rolname = 'artem') THEN
            CREATE USER artem WITH SUPERUSER PASSWORD '123';
            GRANT ALL privileges on database warehouse to artem;
        END IF;
    END
$do$;

-- set role user
SET ROLE artem;
-- create extension for uuid generate
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
-- create schema products
CREATE SCHEMA IF NOT EXISTS products;

-- create tables
CREATE TABLE IF NOT EXISTS products.brand(
  brand_id SERIAL PRIMARY KEY,
  brand_name TEXT NOT NULL
);

COMMENT ON TABLE products.brand is 'хранит марки товаров';
COMMENT ON COLUMN products.brand.brand_id is 'id марки';
COMMENT ON COLUMN products.brand.brand_name is 'название марки';


CREATE TABLE IF NOT EXISTS products.product(
    product_id SERIAL PRIMARY KEY,
    product_name TEXT NOT NULL,
    brand_id INT NOT NULL,
    FOREIGN KEY (brand_id) REFERENCES products.brand(brand_id)
);

COMMENT ON TABLE products.product is 'хранит товары';
COMMENT ON COLUMN products.product.product_id is 'id товара';
COMMENT ON COLUMN products.product.product_name is 'название товара';
COMMENT ON COLUMN products.product.brand_id is 'id марки товара';


CREATE TABLE IF NOT EXISTS products.product_color(
    product_color_id SERIAL PRIMARY KEY,
    product_color_name TEXT NOT NULL
);

COMMENT ON TABLE products.product_color is 'хранит цвета товара';
COMMENT ON COLUMN products.product_color.product_color_id is 'id цвета товара';
COMMENT ON COLUMN products.product_color.product_color_name is 'название цвета товара';


CREATE TABLE IF NOT EXISTS products.product_size(
    product_size_id SERIAL PRIMARY KEY,
    product_size_name TEXT NOT NULL
);

COMMENT ON TABLE products.product_size is 'хранит размеры товара';
COMMENT ON COLUMN products.product_size.product_size_id is 'id размера товара';
COMMENT ON COLUMN products.product_size.product_size_name is 'название размера товара';


CREATE TABLE IF NOT EXISTS products.sku(
    sku_id SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    product_size_id INT NOT NULL,
    product_color_id INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products.product(product_id),
    FOREIGN KEY (product_size_id) REFERENCES products.product_size(product_size_id),
    FOREIGN KEY (product_color_id) REFERENCES products.product_color(product_color_id)
);

COMMENT ON TABLE products.sku is 'складская единица хранения';
COMMENT ON COLUMN products.sku.sku_id is 'id единицы хранения';
COMMENT ON COLUMN products.sku.product_id is 'ссылается на товар';
COMMENT ON COLUMN products.sku.product_size_id is 'ссылается на размер товара';
COMMENT ON COLUMN products.sku.product_color_id is 'ссылается на цвет товара';

-- inserts

INSERT INTO products.product_color(product_color_id, product_color_name) VALUES
(1, 'Blue'),
(2, 'Black')
ON CONFLICT (product_color_id) DO NOTHING;


INSERT INTO products.product_size(product_size_id, product_size_name) VALUES
(1, 'Small'),
(2, 'Medium'),
(2, 'Large')
ON CONFLICT (product_size_id) DO NOTHING;