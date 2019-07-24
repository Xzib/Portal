

INSERT INTO flights(origin,destination,duration) VALUES('Hong Kong','New york','1000');
INSERT INTO flights(origin,destination,duration) VALUES('Karachi','New york','850');
INSERT INTO flights(origin,destination,duration) VALUES('Islamabad','New york','840');
INSERT INTO flights(origin,destination,duration) VALUES('Islamabad','New Delhi','150');
INSERT INTO flights(origin,destination,duration) VALUES('Lahore','Barcelona','2500');

CREATE TABLE passengers(
    id SERIAL primary key,
    name varchar Not Null,
    flights_id INTEGER REFERENCES flights
);




INSERT INTO passengers(name,flights_id) VALUES('Alice','1');
INSERT INTO passengers(name,flights_id) VALUES('Zohaib','1');
INSERT INTO passengers(name,flights_id) VALUES('Faraz','2');
INSERT INTO passengers(name,flights_id) VALUES('Shoaib','2');
INSERT INTO passengers(name,flights_id) VALUES('Asim','3');
INSERT INTO passengers(name,flights_id) VALUES('Siddique','3');
INSERT INTO passengers(name,flights_id) VALUES('Zain','4');
INSERT INTO passengers(name,flights_id) VALUES('Daniyal','4');
INSERT INTO passengers(name,flights_id) VALUES('Kashif','4');