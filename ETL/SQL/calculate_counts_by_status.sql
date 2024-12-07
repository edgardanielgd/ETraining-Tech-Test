SELECT
    D.name as department_name, M.name as municipality_name, 
    G.name as gender_name, T.name as type_name, S.name as status_name, 
    "Contagios" AS tipo,
    COUNT(*) AS count
FROM
    cases C 
    INNER JOIN 
    municipality M ON C.id_municipality = M.id_municipality
    INNER JOIN 
    department D ON M.id_department = D.id_department
    INNER JOIN
    gender G ON G.id_gender = C.id_gender
    INNER JOIN 
    type_contagion T ON T.id_type_contagion = C.id_type_contagion
    INNER JOIN
    status S ON S.id_status = C.id_status

GROUP BY
    D.name, M.name, G.name,
    T.name, S.name

UNION ALL

SELECT
    D.name, M.name, G.name,
    T.name, S.name, 
    "Activos" AS tipo,
    COUNT(*) AS count
FROM
    cases C 
    INNER JOIN 
    municipality M ON C.id_municipality = M.id_municipality
    INNER JOIN 
    department D ON M.id_department = D.id_department
    INNER JOIN
    gender G ON G.id_gender = C.id_gender
    INNER JOIN 
    type_contagion T ON T.id_type_contagion = C.id_type_contagion
    INNER JOIN
    status S ON S.id_status = C.id_status
WHERE
    S.id_status = 0
GROUP BY
    D.name, M.name, G.name,
    T.name, S.name

UNION ALL

SELECT
    D.name, M.name, G.name,
    T.name, S.name, 
    "Fallecidos" AS tipo,
    COUNT(*) AS count
FROM
    cases C 
    INNER JOIN 
    municipality M ON C.id_municipality = M.id_municipality
    INNER JOIN 
    department D ON M.id_department = D.id_department
    INNER JOIN
    gender G ON G.id_gender = C.id_gender
    INNER JOIN 
    type_contagion T ON T.id_type_contagion = C.id_type_contagion
    INNER JOIN
    status S ON S.id_status = C.id_status
WHERE
    S.id_status = 1
GROUP BY
    D.name, M.name, G.name,
    T.name, S.name

UNION ALL

SELECT
    D.name, M.name, G.name,
    T.name, S.name, 
    "Recuperados" AS tipo,
    COUNT(*) AS count
FROM
    cases C 
    INNER JOIN 
    municipality M ON C.id_municipality = M.id_municipality
    INNER JOIN 
    department D ON M.id_department = D.id_department
    INNER JOIN
    gender G ON G.id_gender = C.id_gender
    INNER JOIN 
    type_contagion T ON T.id_type_contagion = C.id_type_contagion
    INNER JOIN
    status S ON S.id_status = C.id_status
WHERE
    S.id_status = 2
GROUP BY
    D.name, M.name, G.name,
    T.name, S.name