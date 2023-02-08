"""Команды создания таблиц в схеме базы данных"""
CREATE_BRAND_TABLE = \
    """
    CREATE TABLE IF NOT EXISTS products.brand(
      brand_id SERIAL PRIMARY KEY,
      brand_name TEXT NOT NULL
    );"""


CREATE_PRODUCT_TABLE = \
    """
    CREATE TABLE IF NOT EXISTS products.product(
        product_id SERIAL PRIMARY KEY,
        product_name TEXT NOT NULL,
        brand_id INT NOT NULL,
        FOREIGN KEY (brand_id) REFERENCES products.brand(brand_id)
    );"""


CREATE_PRODUCT_COLOR_TABLE = \
    """
    CREATE TABLE IF NOT EXISTS products.product_color(
        product_color_id SERIAL PRIMARY KEY,
        product_color_name TEXT NOT NULL
    );"""


CREATE_PRODUCT_SIZE_TABLE = \
    """
    CREATE TABLE IF NOT EXISTS products.product_size(
        product_size_id SERIAL PRIMARY KEY,
        product_size_name TEXT NOT NULL
    );"""


CREATE_SKU_TABLE = \
    """
    CREATE TABLE IF NOT EXISTS products.sku(
        sku_id SERIAL PRIMARY KEY,
        product_id INT NOT NULL,
        product_size_id INT NOT NULL,
        product_color_id INT NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products.product(product_id),
        FOREIGN KEY (product_size_id) REFERENCES products.product_size(product_size_id),
        FOREIGN KEY (product_color_id) REFERENCES products.product_color(product_color_id)
    );"""


COLOR_INSERT = \
    """
    INSERT INTO products.product_color(product_color_id, product_color_name) VALUES
    (1, 'Blue'),
    (2, 'Black')
    ON CONFLICT (product_color_id) DO NOTHING;"""


SIZE_INSERT = \
    """
    INSERT INTO products.product_size(product_size_id, product_size_name) VALUES
    (1, 'Small'),
    (2, 'Medium'),
    (2, 'Large')
    ON CONFLICT (product_size_id) DO NOTHING;"""
