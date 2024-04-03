CREATE VIEW viewAlunosEntre30a32 AS
	SELECT E.nome_aluno, E.idade_aluno,T.nome_turma from estudante as E
		join turma AS T 
        ON E.fk_turma = T.id_turma 
        WHERE E.idade_aluno <= 30 AND E.idade_aluno >= 32 
        ORDER BY E.nome_aluno;
        
select * from viewAlunosEntre30a32;

create role carrasco;

Grant select, insert, update
	on estudante
    to carrasco;
    
grant carrasco to diretor;

grant all on escola to diretor;

create trigger trg_AlteraAIdadeDosVeio
	after update on turma
	for each row
			update estudante
            set idade_aluno = idade_aluno + 1
            where fk_turma=1;
            
select * from escola.estudante
	where fk_turma=1;
    
update turma 
	set ano_turma=2020
    where id_turma=1;

create procedure getIdadeAluno
	(in idade int)
    select *
		from estudante
        where idade_aluno = idade;
        
call getIdadeAluno(30);