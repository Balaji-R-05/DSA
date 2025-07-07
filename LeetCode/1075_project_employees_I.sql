-- 1075. Project Employees I

select project_id, round(avg(experience_years), 2) as average_years from project p, employee e where p.employee_id = e.employee_id group by project_id;