----
-- phpLiteAdmin database dump (http://www.phpliteadmin.org/)
-- phpLiteAdmin version: 1.9.7.1
-- Exported: 11:25am on October 14, 2020 (UTC)
-- database file: /home/ubuntu/project/pcm.db
----
BEGIN TRANSACTION;

----
-- Drop table for casos
----
DROP TABLE IF EXISTS "casos";

----
-- Table structure for casos
----
CREATE TABLE 'casos' ('id' integer PRIMARY KEY NOT NULL, 'result' varchar(10), 'age' smallint, 'contacts' smallint, 'email' varchar(150), 'telephone' integer, 'alt_telephone' integer, 'province' varchar(15), 'qrHouse' smallint, 'nrHouse' smallint, 'address' varchar(150), 'gender' varchar(150), 'obs' text, 'userid' smallint, 'regdate' date, 'status' char(1));

----
-- Data dump for casos, a total of 11 rows
----
INSERT INTO "casos" ("id","result","age","contacts","email","telephone","alt_telephone","province","qrHouse","nrHouse","address","gender","obs","userid","regdate","status") VALUES ('1','Positivo','23','23','julio.rafael@ins.gov.mz','8364747643',NULL,'Sofala',NULL,NULL,NULL,'Masculino',NULL,NULL,NULL,'d');
INSERT INTO "casos" ("id","result","age","contacts","email","telephone","alt_telephone","province","qrHouse","nrHouse","address","gender","obs","userid","regdate","status") VALUES ('2','Negativo','32','100','julio.rafael@ins.gov.mz','87687687687',NULL,'Maputo Provincia',NULL,NULL,NULL,'Masculino',NULL,NULL,NULL,'r');
INSERT INTO "casos" ("id","result","age","contacts","email","telephone","alt_telephone","province","qrHouse","nrHouse","address","gender","obs","userid","regdate","status") VALUES ('3','Positivo','2','23','julio.rafael@ins.gov.mz','324234324','324234324','Gaza','23','34','Loonasnd ask','Masculino','lkjasdlkjalskdja',NULL,NULL,'d');
INSERT INTO "casos" ("id","result","age","contacts","email","telephone","alt_telephone","province","qrHouse","nrHouse","address","gender","obs","userid","regdate","status") VALUES ('4','Negativo','12','4545','abac@akjskasjk','453224323','2342342343','Inhambane','12','12','sadasdadsa','Feminino','121dsadas asda',NULL,NULL,'r');
INSERT INTO "casos" ("id","result","age","contacts","email","telephone","alt_telephone","province","qrHouse","nrHouse","address","gender","obs","userid","regdate","status") VALUES ('5','Positivo','23','34','ja@kajs.com','845989898','845989898','Maputo Cidade','129','23','Miuiaskd askjdsank','Masculino','Lohaskjd asjdk askjdhsa',NULL,NULL,NULL);
INSERT INTO "casos" ("id","result","age","contacts","email","telephone","alt_telephone","province","qrHouse","nrHouse","address","gender","obs","userid","regdate","status") VALUES ('6','Positivo','33','322','julio.rafael@ins.gov.mz','122312312','122312312','Nampula','1','23','kalshdas salkdjsald salkjdsad','Feminino','janmshdkjsa sakdjhsakjdhsa',NULL,NULL,'d');
INSERT INTO "casos" ("id","result","age","contacts","email","telephone","alt_telephone","province","qrHouse","nrHouse","address","gender","obs","userid","regdate","status") VALUES ('7','Negativo','13','343','','983874658','','Nampula','','','','Masculino','',NULL,NULL,NULL);
INSERT INTO "casos" ("id","result","age","contacts","email","telephone","alt_telephone","province","qrHouse","nrHouse","address","gender","obs","userid","regdate","status") VALUES ('8','Positivo','46','2342','','859834938','','Gaza','','','','Feminino','','1','2020-10-01',NULL);
INSERT INTO "casos" ("id","result","age","contacts","email","telephone","alt_telephone","province","qrHouse","nrHouse","address","gender","obs","userid","regdate","status") VALUES ('9','Negativo','66','50','','873399223','','Tete','','','','Masculino','Oaskdh akjshdkasj askjdhakjsd askdhsalkdas','2','2020-10-01',NULL);
INSERT INTO "casos" ("id","result","age","contacts","email","telephone","alt_telephone","province","qrHouse","nrHouse","address","gender","obs","userid","regdate","status") VALUES ('10','Positivo','100','11','','212218967','','Inhambane','23','876','Mulbb Bb sdfsdfsdfsd','Feminino','','2','2020-10-01',NULL);
INSERT INTO "casos" ("id","result","age","contacts","email","telephone","alt_telephone","province","qrHouse","nrHouse","address","gender","obs","userid","regdate","status") VALUES ('11','Negativo','45','232','','967652376','','Gaza','','','','Feminino','','2','2020-10-01',NULL);

----
-- Drop table for utilizadores
----
DROP TABLE IF EXISTS "utilizadores";

----
-- Table structure for utilizadores
----
CREATE TABLE 'utilizadores' ('id' integer PRIMARY KEY NOT NULL, 'name' varchar(150), 'username' varchar(150), 'password' varchar(150), 'regdate' date);

----
-- Data dump for utilizadores, a total of 2 rows
----
INSERT INTO "utilizadores" ("id","name","username","password","regdate") VALUES ('1','Júlio Rafael','user','pbkdf2:sha256:150000$Q2Rl9nVF$9f77e4ade5f6d7f74e78b4fc4ea333b534d1749e1d81b154c25f8fe74debc561','2020-10-01');
INSERT INTO "utilizadores" ("id","name","username","password","regdate") VALUES ('2','Debora Evelyn Rafael','debora','pbkdf2:sha256:150000$JvtTuhnL$8148c1c8f7b8f8b69c4615597b71c4dc958f9f54137d4234a6c23a030ceb9f26','2020-10-01');
COMMIT;
