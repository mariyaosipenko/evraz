create table kafka(
  id int,
  message varchar(300)
);

create table kafkainfo(
  code_id int primary key,
  algotype varchar(30),
  algoA int,
  algoB int,
  value varchar(50),
  time timestamp
);

create table type (typename_id int primary key, typename varchar(30));
insert into type (typename_id, typename) values (1, 'Температура нагрева');
insert into type (typename_id, typename) values (2, 'Вибрация');

create table podtype (podtype_id int primary key, typename varchar(30));
insert into podtype (podtype_id, typename) values (1, 'Температура');
insert into podtype (podtype_id, typename) values (2, 'Уставки');
insert into podtype (podtype_id, typename) values (3, 'Осевая');
insert into podtype (podtype_id, typename) values (4, 'Горизонтальная');
insert into podtype (podtype_id, typename) values (5, 'Вертикальная');

create table signal (signal_id int primary key, typename varchar(30));
insert into signal (signal_id, typename) values (1, 'temperature');
insert into signal (signal_id, typename) values (2, 'alarm_max');
insert into signal (signal_id, typename) values (3, 'alarm_min');
insert into signal (signal_id, typename) values (4, 'warning_max');
insert into signal (signal_id, typename) values (5, 'warning_min');

create table info(
  id int,
  code_id int,
  name varchar(200),
  typename_id int,
  podtype_id int,
  signal_id int,
  analog boolean,
  activity int,
  FOREIGN KEY (typename_id)  REFERENCES type(typename_id),
  FOREIGN KEY (podtype_id)  REFERENCES podtype(podtype_id),
  FOREIGN KEY (signal_id)  REFERENCES signal(signal_id),
  FOREIGN KEY (code_id)  REFERENCES kafkainfo(code_id)
);