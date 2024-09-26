create table if not exists countries (
    country_id serial primary key,
    country_name varchar(100) unique
);

create table if not exists cities (
    city_id serial primary key,
    city_name varchar(100),
    country_id int not null,
    foreign key (country_id) references countries(country_id)
);

create table if not exists target_types (
    target_type_id serial primary key,
    target_type_name varchar(255) unique
);

create table if not exists locations (
	location_id serial primary key,
	latitude decimal,
    longitude decimal
);


create table if not exists targets (
    target_id serial primary key,
    target_industry varchar(255),
    city_id int,
    target_type_id int,
	target_priority int,
	location_id int,
    foreign key (city_id) references cities(city_id),
    foreign key (target_type_id) references target_types (target_type_id),
	foreign key (location_id) references locations (location_id)
);
