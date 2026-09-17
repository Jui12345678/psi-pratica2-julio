Os modelos ORM estão no arquivo models.py. Nele foram criadas as classes Autor e Livro, que representam as tabelas do banco de dados.

A classe Autor representa o lado um, porque um autor pode possuir vários livros. A classe Livro representa o lado "muitos", pois vários livros podem pertencer ao mesmo autor.

O ForeignKey("autores.id") estabelece a ligação entre as tabelas.
