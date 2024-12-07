START TRANSACTION;

CREATE TABLE department (
    id_department INT PRIMARY KEY NOT NULL,
    name VARCHAR(45) NOT NULL
);

CREATE TABLE municipality (
    id_municipality INT PRIMARY KEY NOT NULL,
    name VARCHAR(200) NOT NULL,
    id_department INT NOT NULL,

    FOREIGN KEY (id_department)
        REFERENCES department(id_department)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE gender (
    id_gender INT PRIMARY KEY NOT NULL,
    name VARCHAR(200) NOT NULL
);

CREATE TABLE type_contagion (
    id_type_contagion INT PRIMARY KEY NOT NULL,
    name VARCHAR(200) NOT NULL
);

CREATE TABLE status (
    id_status INT PRIMARY KEY NOT NULL,
    name VARCHAR(200) NOT NULL
);

CREATE TABLE cases (
    id_case INT PRIMARY KEY NOT NULL,
    id_municipality INT NOT NULL,
    age INT NOT NULL,
    id_gender INT NOT NULL,
    id_type_contagion INT NOT NULL,
    id_status INT NOT NULL,
    date_sympthom DATETIME NULL,
    date_death DATETIME NULL,
    date_diagnosis DATETIME NULL,
    date_recovery DATETIME NULL,

    FOREIGN KEY (id_municipality)
        REFERENCES municipality(id_municipality)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    FOREIGN KEY (id_gender)
        REFERENCES gender(id_gender)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    FOREIGN KEY (id_type_contagion)
        REFERENCES type_contagion(id_type_contagion)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    FOREIGN KEY (id_status)
        REFERENCES status(id_status)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

COMMIT;