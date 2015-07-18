drop table if exists questions;
create table questions (
  id integer primary key autoincrement,
  title text not null,
  text text not null
);

drop table if exists response;
create table response (
  id integer primary key autoincrement,
  text text not null,
  question integer not null,
  archetype integer not null
);

drop table if exists archetype;
create table archetype (
  id integer primary key autoincrement,
  label text not null,
  description text not null
);

