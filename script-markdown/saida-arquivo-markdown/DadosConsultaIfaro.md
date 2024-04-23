| Atributo                    | Tipo        | Descrição                                               |
|:----------------------------|:------------|:--------------------------------------------------------|
| _id                         | ObjectIid   | Identificador único do registro                         |
| DataValidadeConsulta        | datetime    | Data da validade da consulta                            |
| TipoRetorno                 | int         | Tipo do retorno do parceiro Ifaro. 0 = Sucesso          |
| Nome                        | string      | Nome da pessoa                                          |
| Cpf                         | string      | Cpf da pessoa                                           |
| Rg                          | string      | Rg da pessoa                                            |
| RgOrgaoEmissor              | string      | Orgão emissor do Rg                                     |
| RgUfEmissao                 | string      | Uf da Emissão                                           |
| RgDataEmissao               | datetime    | Data da emissão                                         |
| DataNascimento              | string      | Data de nascimento da pessoa                            |
| Idade                       | string      | Idade da pessoa                                         |
| Signo                       | string      | Signo da pessoa                                         |
| Sexo                        | string      | Sexo da pessoa                                          |
| Mae                         | string      | Mãe da pessoa                                           |
| Telefones                   | ArrayObject | Array de objetos contendo numeros de telefone da pessoa |
| Telefones.Numero            | string      | Numero de telefone da pessoa                            |
| Telefones.Dd                | string      | Dd da pessoa                                            |
| Telefones.Operadora         | string      | Operado do telefone da pessoa                           |
| Telefones.Tipo              | string      | Tipo do telefone. Se é móvel ou fixo                    |
| Telefones.Ranking           | int         | Ranking que o objeto está na lista                      |
| Telefones.Data              | string      | Data de emissão do telefone                             |
| Emails                      | ArrayObject | Array de objetos contendo os emails da pessoa           |
| Emails.EmailEndereco        | string      | endereço de email da pessoa                             |
| Emails.Ranking              | int         | Ranking que o objeto está na lista                      |
| Emails.Data                 | string      | Data da emissão do email                                |
| Enderecos                   | ArrayObject | Array de objetos contendo endereços da pessoa           |
| Enderecos.Logadouro         | string      | Nome do logradouro                                      |
| Enderecos.Numero            | string      | Número do logradouro                                    |
| Enderecos.Bairro            | string      | Bairro do logradouro                                    |
| Enderecos.Cidade            | string      | Cidade                                                  |
| Enderecos.Uf                | string      | Uf do logradouro                                        |
| Enderecos.Cep               | string      | Cep do logradouro                                       |
| Enderecos.Complemento       | string      | Complemento do logradouro                               |
| Enderecos.Ranking           | int         | Ranking que o objeto está na lista                      |
| Enderecos.Latitude          | int         | Latitude do logradouro                                  |
| Enderecos.Longitude         | int         | Longitude do logradouro                                 |
| Enderecos.Ddd               | int         | DDD do logradouro                                       |
| Enderecos.LogadouroTipo     | string      | Tipo do logradouro                                      |
| Enderecos.LogadouroCompleto | string      | Logradouro Completo                                     |
| Enderecos.Ibge_Cod_Uf       | int         | Codigo Ibge UF                                          |
| Enderecos.Ibge_Cod_Cidade   | int         | Codigo ibge Cidade                                      |
| Enderecos.Data              | string      | Data do logradouro                                      |