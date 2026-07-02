SELECT
    t.request_at AS Day,
    ROUND(
        SUM(t.status <> 'completed') / COUNT(*),
        2
    ) AS `Cancellation Rate`
FROM Trips t
JOIN Users client
    ON t.client_id = client.users_id
JOIN Users driver
    ON t.driver_id = driver.users_id
WHERE client.banned = 'No'
  AND driver.banned = 'No'
  AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at;