/*
 * schema.sql
 * Copyright (C) 2016 becxer <becxer87@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */ 


-- vim:et


drop table if exists users;
drop table if exists posts;

create table users(
    no integer primary key autoincrement,
    name string not null,
    id string not null unique,
    password string not null
);

create table posts(
    no integer primary key autoincrement,
    title string not null,
    content string,
    files string not null
);

insert into users(name, id, password) values ('tester1', 'test1', '1234');
insert into users(name, id, password) values ('tester2', 'test2', '1234');
insert into users(name, id, password) values ('tester3', 'test3', '1234');

insert into posts(title, content, files) values ('test post1', 'test content', '');
insert into posts(title, content, files) values ('test post2', 'test content', '');
insert into posts(title, content, files) values ('test post3', 'test content', '');
