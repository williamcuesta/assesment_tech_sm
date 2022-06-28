-- DROP DATABASE IF EXISTS prueba_sm;
-- CREATE DATABASE prueba_sm;
USE prueba_sm;

-- first table PP_users
CREATE TABLE `prueba_sm`.`PP_users` (
    `u`             int not null,
    `techniques`    text(500),
    `items`         text(500),
    `n_items`       int,
    `ratings`       text(500),
    `n_ratings`     int,
    constraint pk_u primary key( `u`)
);

-- table RAW_recipes
CREATE TABLE `prueba_sm`.`RAW_recipes` (
    `id`             int not null,
    `name`           text(500),
    `minutes`        int,
    `contributor_id` int,
    `submitted`      text(500),
    `tags`           text(500),
    `nutrition`      text(500),
    `n_steps`        int,
    `steps`          text(500),
    `description`    text(500),
    `ingredients`    text(500),
    `n_ingredients`  int,
    constraint pk_id primary key(`id`)
);

-- table PP_recipes
CREATE TABLE `prueba_sm`.`PP_recipes` (
    `i`                    int not null,
    `id_`                   int not null,
    `name_tokens`          text(500),
    `ingredient_tokens`    text(500),
    `steps_tokens`         text(500),
    `techniques`           text(500),
    `calorie_level`        int,
    `ingredient_ids`       text(500),
    constraint pk_i primary key( `i`)
);

-- table RAW_interactions
CREATE TABLE `prueba_sm`.`RAW_interactions` (
	`user_id`		int,
    `recipe_id`		int not null,
    `date`			datetime,
    `review`		text(500),
    constraint fk_recibe_id foreign key(`recipe_id`) references `PP_recipes`(`i`) on update cascade
);

-- SELECT * FROM RAW_interactions;

-- select COUNT(*) from RAW_interactions;



