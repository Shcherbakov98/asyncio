CREATE TABLE user_favorite(
    user_id int not null,
    product_id int not null
);
INSERT INTO user_favorite (user_id, product_id) VALUES (1, 1);
INSERT INTO user_favorite (user_id, product_id) VALUES (1, 2);
INSERT INTO user_favorite (user_id, product_id) VALUES (1, 3);
INSERT INTO user_favorite (user_id, product_id) VALUES (3, 1);
INSERT INTO user_favorite (user_id, product_id) VALUES (3, 2);
INSERT INTO user_favorite (user_id, product_id) VALUES (3, 3);