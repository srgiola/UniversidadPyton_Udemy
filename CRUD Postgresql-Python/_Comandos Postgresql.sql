PostgreSQL 
-No es case sensitive con las palabras reservadas-

<> indica que va algo entre ellos
<Schema> Puede ser omitido si se utiliza el Schema Public

select * from "<Schema>.<Table>"
	select * from Persona

select * from "<Schema>.<Table>" where "<Campo>" <Condición>
	select * from "Persona" where "ID" = 1

select * from "<Schema>.<Table>" order by "<Campo>" <Instrucción>
	select * from "Persona" order by "Id_Persona" desc
	select * from "Persona" order by "Id_Persona" asc
	
insert into "<Schema>.<Table>"("<Campo>") values("<Valor a insertar>")
	insert into "Persona"("Nombre") values('Susana')
	insert into "Persona"("Nombre", "Email") values('Susana', 'slara@gmail.com')

update "<Schema>.<Table>" set "<Campo>" = <Valor>, "<Campo>" = <Valor> where <Condicion>
	update "Persona" set "Nombre" = 'Ivone', "Email" = 'ipa@gail.com' where "Id_Persona" = 3

delete from "<Schema>.<Table>"
	delete from "Persona"

delete from "<Schema>.<Table>" where <Condicion>
	delete from "Persona" where "ID" = 3