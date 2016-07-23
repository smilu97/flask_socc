/*
 * schema.sql
 * Copyright (C) 2016 becxer <becxer87@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */ 


-- vim:et


drop table if exists users;
drop table if exists posts

create table users(
    no integer primary key autoincrement,
    name string not null,
    id string not null,
    password string not null
);

create table posts(
    no integer primary key autoincrement,
    title string not null,
    content string,
    files string not null
);
