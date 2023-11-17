CREATE TABLE user_cart(
    user_id int not null,
    product_id int not null
)
INSERT INTO user_cart (user_id, product_id) VALUES (1, 1);
INSERT INTO user_cart (user_id, product_id) VALUES (1, 2);
INSERT INTO user_cart (user_id, product_id) VALUES (1, 3);
INSERT INTO user_cart (user_id, product_id) VALUES (2, 1);
INSERT INTO user_cart (user_id, product_id) VALUES (2, 2);
INSERT INTO user_cart (user_id, product_id) VALUES (2, 5);