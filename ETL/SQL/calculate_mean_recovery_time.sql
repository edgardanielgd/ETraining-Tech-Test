SELECT
    D.name as department_name, M.name as municipality_name, 
    G.name as gender_name, T.name as type_name,
    TIMESTAMPDIFF(HOUR, C.date_symptom, C.date_recovery) AS recovery_time
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
    T.name