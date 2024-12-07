SELECT
    D.name as department_name, M.name as municipality_name, 
    G.name as gender_name, T.name as type_name,
    SUM(
        CASE S.id_status WHEN 1 THEN 1 ELSE 0 END
    ) AS death_count,
    COUNT(*) AS total_count
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
    T.name