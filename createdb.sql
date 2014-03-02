create database unit;
\c unit
create table person (
  id bigserial primary key,
  regist_time timestamp default now(),
  active_time timestamp,
  active_state boolean,
  email varchar(64) unique not null,
  old_email varchar(64),
  password varchar(32),
  province smallint,
  city smallint,
  sex boolean,
  phone varchar(16),
  IDcard varchar(20),
  nick varchar(32)[10],
  default_nick varchar(32),
  portrait varchar(128)
);
create table company (
  id bigserial primary key,
  name varchar(64) unique not null,
  dept varchar(32)[],
  brief text,
  portrait varchar(128),

  rating real,
  class varchar(32)[],
  webpage varchar(128),
  build_time timestamp,
  address varchar(256),
  tag varchar(32)[],

  comments integer
);
create table suggestion (
  id bigserial primary key,
  uid bigint not null,
  s_time timestamp default now(),
  suggestion text
);


-- sub-library, when info is too large
create database info;
\c info
create table comment (
  id bigserial primary key,
  cid bigint not null,
  uid bigint not null,
  pub_time timestamp default now(),
  rating smallint check (rating in (0,1,2,3,4,5)),
  nick varchar(32),
  content text
);
create index company_time on comment (cid, pub_time);
create index user_comment on comment (uid);

