ALTER SESSION SET NLS_DATE_FORMAT = 'DD.MM.YYYY';

CREATE TABLE Wampiry
(pseudo_wampira VARCHAR2(15) CONSTRAINT w_pw_pr PRIMARY KEY,
wampir_w_rodzinie  DATE CONSTRAINT w_wr_ob NOT NULL,
plec_wampira CHAR(1) CONSTRAINT w_plw_ob CHECK(plec_wampira IN ('K','M')) NOT NULL,
pseudo_szefa VARCHAR2(15) CONSTRAINT w_ps_obc REFERENCES Wampiry(pseudo_wampira)
);

CREATE TABLE Zlecenia
(nr_zlecenia NUMBER(6) CONSTRAINT z_nz_pr PRIMARY KEY CHECK(nr_zlecenia > 0),
data_zlecenia DATE CONSTRAINT z_dz_ob NOT NULL,
pseudo_wampira VARCHAR2(15) CONSTRAINT z_pw_obc REFERENCES Wampiry(pseudo_wampira)
);

CREATE TABLE Dawcy
(pseudo_dawcy VARCHAR2(15)CONSTRAINT d_pd_pr PRIMARY KEY,
rocznik_dawcy NUMBER(6) CONSTRAINT d_rd_ob NOT NULL,
plec_dawcy CHAR(1) CONSTRAINT d_pd_ob CHECK(plec_dawcy IN ('K','M')) NOT NULL,
grupa_krwi CHAR(2) CONSTRAINT d_gk_obc2 CHECK(grupa_krwi IN ('0','A','B','AB')) NOT NULL
);

--Drop TABLE Donacje;
CREATE TABLE Donacje
(nr_zlecenia NUMBER(6) CONSTRAINT d_nz_obc REFERENCES Zlecenia(nr_zlecenia),
pseudo_dawcy VARCHAR2(15)CONSTRAINT d_pd_obc REFERENCES Dawcy(pseudo_dawcy),
data_oddania DATE CONSTRAINT d_od_ob NOT NULL,
ilosc_krwi NUMBER(3) CONSTRAINT d_ik_ran CHECK(ilosc_krwi > 0),
pseudo_wampira VARCHAR2(15)CONSTRAINT d_pw_ref REFERENCES Wampiry(pseudo_wampira),
data_wydania DATE,
CONSTRAINT d_nz_pr Primary Key(nr_zlecenia, pseudo_dawcy)
);

ALTER TABLE Donacje 
 ADD CONSTRAINT data_wydania 
 CHECK (data_wydania >= data_oddania);

CREATE TABLE Sprawnosci
(sprawnosc VARCHAR2(20) CONSTRAINT s_sp_pr PRIMARY KEY);

CREATE TABLE Sprawnosci_w
(pseudo_wampira VARCHAR2(15) CONSTRAINT sp_pw_pr REFERENCES Wampiry(pseudo_wampira),
sprawnosc VARCHAR2(20) CONSTRAINT sp_sp_pr REFERENCES Sprawnosci(sprawnosc),
sprawnosc_od DATE CONSTRAINT sp_so_ob NOT NULL,
CONSTRAINT sp_stw_pr Primary Key(pseudo_wampira, sprawnosc)
);

--DROP TABLE Jezyki_obce;
CREATE TABLE Jezyki_obce
(jezyk_obcy VARCHAR2(20) CONSTRAINT jo_joa_pr PRIMARY KEY);
--DELETE FROM Jezyki_obce;


CREATE TABLE Jezyki_obce_w
(pseudo_wampira VARCHAR2(15) CONSTRAINT jow_pw_pr1 REFERENCES Wampiry(pseudo_wampira),
jezyk_obcy VARCHAR2(20) CONSTRAINT jow_jo_pr1 REFERENCES Jezyki_obce(jezyk_obcy),
jezyk_obcy_od DATE CONSTRAINT jow_joo_ob1 NOT NULL,
CONSTRAINT jow_doda_p1r Primary Key(pseudo_wampira, jezyk_obcy)
);




INSERT All 
INTO Wampiry(pseudo_wampira,wampir_w_rodzinie,plec_wampira,pseudo_szefa) VALUES('Drakula','12.12.1217','M',NULL)
INTO Wampiry(pseudo_wampira,wampir_w_rodzinie,plec_wampira,pseudo_szefa) VALUES('Opoj','07.11.1777','M','Drakula')
INTO Wampiry(pseudo_wampira,wampir_w_rodzinie,plec_wampira,pseudo_szefa) VALUES('Wicek','11.11.1721','M','Drakula')
INTO Wampiry(pseudo_wampira,wampir_w_rodzinie,plec_wampira,pseudo_szefa) VALUES('Baczek','13.04.1855','M','Opoj')
INTO Wampiry(pseudo_wampira,wampir_w_rodzinie,plec_wampira,pseudo_szefa) VALUES('Bolek','31.05.1945','M','Opoj')
INTO Wampiry(pseudo_wampira,wampir_w_rodzinie,plec_wampira,pseudo_szefa) VALUES('Gacek','21.02.1891','M','Wicek')
INTO Wampiry(pseudo_wampira,wampir_w_rodzinie,plec_wampira,pseudo_szefa) VALUES('Pijawka','03.11.1901','K','Wicek')
INTO Wampiry(pseudo_wampira,wampir_w_rodzinie,plec_wampira,pseudo_szefa) VALUES('Czerwony','13.09.1823','M','Wicek')
INTO Wampiry(pseudo_wampira,wampir_w_rodzinie,plec_wampira,pseudo_szefa) VALUES('Komar','23.07.1911','M','Wicek')
INTO Wampiry(pseudo_wampira,wampir_w_rodzinie,plec_wampira,pseudo_szefa) VALUES('Zyleta','23.09.1911','K','Opoj')
INTO Wampiry(pseudo_wampira,wampir_w_rodzinie,plec_wampira,pseudo_szefa) VALUES('Predka','29.03.1877','K','Drakula')
SELECT 1 FROM Dual;

SELECT * FROM Wampiry;

INSERT ALL
INTO Zlecenia(nr_zlecenia,data_zlecenia,pseudo_wampira) VALUES(221,'04.07.2005','Opoj')
INTO Zlecenia(nr_zlecenia,data_zlecenia,pseudo_wampira) VALUES(222,'04.07.2005','Baczek')
INTO Zlecenia(nr_zlecenia,data_zlecenia,pseudo_wampira) VALUES(223,'17.07.2005','Bolek')
INTO Zlecenia(nr_zlecenia,data_zlecenia,pseudo_wampira) VALUES(224,'22.07.2005','Opoj')
INTO Zlecenia(nr_zlecenia,data_zlecenia,pseudo_wampira) VALUES(225,'01.08.2005','Pijawka')
INTO Zlecenia(nr_zlecenia,data_zlecenia,pseudo_wampira) VALUES(226,'07.08.2005','Gacek')
SELECT 1 FROM Dual;

INSERT ALL
INTO Dawcy(pseudo_dawcy,rocznik_dawcy,plec_dawcy,grupa_krwi) VALUES('Slodka',1966,'K','AB')
INTO Dawcy(pseudo_dawcy,rocznik_dawcy,plec_dawcy,grupa_krwi) VALUES('Miodzio',1983,'M','B')
INTO Dawcy(pseudo_dawcy,rocznik_dawcy,plec_dawcy,grupa_krwi) VALUES('Gorzka',1958,'K','0')
INTO Dawcy(pseudo_dawcy,rocznik_dawcy,plec_dawcy,grupa_krwi) VALUES('Lolita',1987,'K','0')
INTO Dawcy(pseudo_dawcy,rocznik_dawcy,plec_dawcy,grupa_krwi) VALUES('Wytrawny',1971,'M','A')
INTO Dawcy(pseudo_dawcy,rocznik_dawcy,plec_dawcy,grupa_krwi) VALUES('Okocim',1966,'M','B')
INTO Dawcy(pseudo_dawcy,rocznik_dawcy,plec_dawcy,grupa_krwi) VALUES('Adonis',1977,'M','AB')
INTO Dawcy(pseudo_dawcy,rocznik_dawcy,plec_dawcy,grupa_krwi) VALUES('Zywiec',1969,'M','A')
INTO Dawcy(pseudo_dawcy,rocznik_dawcy,plec_dawcy,grupa_krwi) VALUES('Eliksir',1977,'M','0')
INTO Dawcy(pseudo_dawcy,rocznik_dawcy,plec_dawcy,grupa_krwi) VALUES('Zenek',1959,'M','B')
INTO Dawcy(pseudo_dawcy,rocznik_dawcy,plec_dawcy,grupa_krwi) VALUES('Zoska',1963,'K','0')
INTO Dawcy(pseudo_dawcy,rocznik_dawcy,plec_dawcy,grupa_krwi) VALUES('Czerwonka',1953,'M','A')
SELECT 1 FROM Dual;

INSERT ALL
INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES(221,'Slodka','04.07.2005',455,'Drakula','06.08.2005')
INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES(221,'Miodzio','04.07.2005',680,'Gacek','15.08.2005')
INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES(221,'Gorzka','05.07.2005',471,'Pijawka','11.08.2005')
INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES(221,'Lolita','05.07.2005',340,'Czerwony','21.08.2005')
INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES(222,'Wytrawny','07.07.2005',703,'Drakula','17.07.2005')
INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES(222,'Okocim','07.07.2005',530,'Komar','01.09.2005')
INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES(222,'Adonis','08.07.2005',221,'Zyleta','11.09.2005')
INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES(223,'Zywiec','17.07.2005',587,'Wicek','18.09.2005')
INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES(224,'Gorzka','22.07.2005',421,'Drakula','23.08.2005')
INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES(224,'Eliksir','25.07.2005',377,'Predka','26.07.2005')
INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES(225,'Zenek','04.08.2005',600,'Opoj','15.08.2005')
INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES(225,'Zoska','06.08.2005',450,NULL,NULL)
INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES(226,'Czerwonka','10.08.2005',517,'Pijawka','30.09.2005')
INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES(226,'Miodzio','11.08.2005',644,NULL,NULL)
SELECT 1 FROM Dual;

INSERT ALL
INTO Sprawnosci(sprawnosc) VALUES('podryw')
INTO Sprawnosci(sprawnosc) VALUES('gorzala')
INTO Sprawnosci(sprawnosc) VALUES('kasa')
INTO Sprawnosci(sprawnosc) VALUES('przymus')
INTO Sprawnosci(sprawnosc) VALUES('niesmiertelnosc')
SELECT 1 FROM Dual;

INSERT ALL
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Drakula','podryw','12.12.1217')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Drakula','gorzala','12.12.1217')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Wicek','kasa','11.11.1721')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Wicek','przymus','07.01.1771')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Opoj','podryw','07.11.1777')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Czerwony','niesmiertelnosc','13.09.1823')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Drakula','kasa','13.09.1823')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Opoj','gorzala','11.12.1844')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Baczek','gorzala','13.04.1855')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Drakula','przymus','14.06.1857')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Drakula','niesmiertelnosc','21.08.1858')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Opoj','przymus','15.07.1861')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Wicek','gorzala','19.01.1866')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Predka','podryw','29.03.1877')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Czerwony','kasa','03.02.1891')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Gacek','kasa','21.02.1891')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Pijawka','podryw','03.11.1901')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Komar','gorzala','23.07.1911')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Zyleta','przymus','23.09.1911')
INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES('Bolek','gorzala','31.05.1945')
SELECT 1 FROM Dual;

INSERT ALL
INTO Jezyki_obce(jezyk_obcy) VALUES('niemiecki')
INTO Jezyki_obce(jezyk_obcy) VALUES('wegierski')
INTO Jezyki_obce(jezyk_obcy) VALUES('bulgarski')
INTO Jezyki_obce(jezyk_obcy) VALUES('rosyjski')
INTO Jezyki_obce(jezyk_obcy) VALUES('portugalski')
INTO Jezyki_obce(jezyk_obcy) VALUES('francuski')
INTO Jezyki_obce(jezyk_obcy) VALUES('angielski')
INTO Jezyki_obce(jezyk_obcy) VALUES('polski')
INTO Jezyki_obce(jezyk_obcy) VALUES('hiszpanski')
INTO Jezyki_obce(jezyk_obcy) VALUES('czeski')
INTO Jezyki_obce(jezyk_obcy) VALUES('wloski')
INTO Jezyki_obce(jezyk_obcy) VALUES('szwedzki')
SELECT 1 FROM Dual;

INSERT ALL
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Drakula','niemiecki','12.12.1217')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Drakula','wegierski','12.12.1217')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Drakula','bulgarski','03.04.1455')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Wicek','rosyjski','11.11.1721')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Opoj','portugalski','07.11.1777')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Czerwony','francuski','13.09.1823')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Drakula','angielski','13.09.1823')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Wicek','polski','18.08.1835')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Opoj','hiszpanski','12.03.1851')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Baczek','czeski','13.04.1855')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Wicek','niemiecki','11.06.1869')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Wicek','wloski','14.03.1873')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Predka','czeski','29.03.1877')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Opoj','polski','13.09.1883')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Czerwony','rosyjski','23.11.1888')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Gacek','polski','21.02.1891')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Predka','niemiecki','07.06.1894')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Baczek','angielski','04.12.1899')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Pijawka','angielski','03.11.1901')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Komar','szwedzki','23.07.1911')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Zyleta','angielski','23.09.1911')
INTO Jezyki_obce_w(pseudo_wampira,jezyk_obcy,jezyk_obcy_od) VALUES('Bolek','francuski','31.05.1945')
SELECT 1 FROM Dual;

--SELECT table_name FROM user_tables;
--SELECT * FROM Jezyki_obce;


--Lista2
--1
SELECT pseudo_dawcy "Dawca A",
    rocznik_dawcy||'    ' "Rocznik"
FROM Dawcy
WHERE grupa_krwi='A';

--2
SELECT DISTINCT pseudo_dawcy "Dawca"
FROM Donacje
WHERE data_oddania BETWEEN '20.07.2005' AND '20.08.2005';

--3
SELECT pseudo_dawcy "Dawca",
    plec_dawcy||'        ' "Plec"
FROM Dawcy
WHERE rocznik_dawcy IN (1971,1977);

--4
SELECT DISTINCT pseudo_dawcy "Dawca"
FROM Donacje
WHERE (data_wydania IS NOT NULL
AND ADD_MONTHS(data_wydania,10) <= TO_DATE('17.05.2006', 'DD.MM.YYYY'));

--5
SELECT pseudo_dawcy "Dawca",
	ilosc_krwi||'  ' "Objetosc",
    NVL(TO_CHAR(data_wydania, 'DD.MM.YYYY'), 'Na stanie') "Wydano"
FROM Donacje
WHERE data_wydania > '10.07.2005';

--6
SELECT COUNT(DISTINCT sprawnosc) "Liczba sprawnosci" --poprawić
FROM Sprawnosci_w
WHERE pseudo_wampira IN ('Opoj','Czerwony');


SELECT SUM(ilosc_krwi) "Cieple buleczki"
FROM Donacje
WHERE data_wydania - data_oddania <= 10;


SELECT pseudo_wampira "Wampir",
    COUNT(*) "liczba jezykow"
FROM Jezyki_obce_w
WHERE jezyk_obcy != 'rosyjski'
GROUP BY pseudo_wampira;


SELECT pseudo_wampira "Wampir",
    COUNT(*) "Liczba konsumpcji"
FROM Donacje
WHERE pseudo_wampira is NOT NULL
GROUP BY pseudo_wampira
HAVING COUNT(*)>1;

SELECT grupa_krwi "Grupa",
	plec_dawcy||'  ' "Plec",
    COUNT(*) "Liczba dawcow"
FROM Dawcy
GROUP BY grupa_krwi, plec_dawcy;

--Lista3

--1
SELECT DISTINCT nr_zlecenia "Zlecenie AB"
FROM Donacje d
JOIN Dawcy daw ON d.pseudo_dawcy = daw.pseudo_dawcy
WHERE daw.grupa_krwi = 'AB';

--2
SELECT w1.pseudo_wampira "PSEUDO WAMPIRA",
w1.plec_wampira "PLEC",
NVL(w2.pseudo_wampira, '  ') "PSEUDO SZEFA",
NVL(w2.plec_wampira, '  ') "PLEC SZEFA"

FROM Wampiry w1
LEFT JOIN Wampiry w2 ON w1.pseudo_szefa = w2.pseudo_wampira
;

--3
SELECT pseudo_dawcy "Dawca_przed_Slodka", plec_dawcy "Plec"
FROM Dawcy 
WHERE rocznik_dawcy < (
SELECT rocznik_dawcy 
FROM Dawcy 
WHERE pseudo_dawcy='Slodka')
;

-- 4
SELECT 
    dona.pseudo_dawcy AS "Pseudonim",
    'Ponizej 700' AS Pobor
FROM Donacje dona
GROUP BY dona.pseudo_dawcy
HAVING SUM(dona.ilosc_krwi) < 700

UNION

SELECT 
    dona.pseudo_dawcy AS "Pseudonim",
    'Miedzy 700 a 1000' AS Pobor
FROM Donacje dona
GROUP BY dona.pseudo_dawcy
HAVING SUM(dona.ilosc_krwi) BETWEEN 700 AND 1000

UNION

SELECT 
    dona.pseudo_dawcy AS "Pseudonim",
    'Powyżej 1000' AS Pobor
FROM Donacje dona
GROUP BY dona.pseudo_dawcy
HAVING SUM(dona.ilosc_krwi) > 1000
ORDER BY 1;

--5
SELECT 
    SP.pseudo_wampira AS Wampir,
    COUNT(DISTINCT SP.sprawnosc) AS Liczba
FROM 
    Sprawnosci_w SP
JOIN (
    SELECT 
        JO.pseudo_wampira,
        COUNT(DISTINCT JO.jezyk_obcy) AS liczba_jezykow
    FROM 
        Jezyki_obce_w JO
    GROUP BY 
        JO.pseudo_wampira
    ) j 
ON SP.pseudo_wampira = j.pseudo_wampira
GROUP BY 
    SP.pseudo_wampira, j.liczba_jezykow
HAVING 
    COUNT(DISTINCT SP.sprawnosc) = j.liczba_jezykow
ORDER BY 
    SP.pseudo_wampira;

--6

SELECT 
    nr_zlecenia AS "Zlecenie AB", 
    data_oddania AS "Data wykonania"
FROM Donacje 
WHERE pseudo_dawcy IN 
(SELECT pseudo_dawcy FROM Dawcy
WHERE grupa_krwi='AB')
ORDER BY nr_zlecenia;

--7
SELECT 
    W.plec_wampira AS Plec,
    COUNT(*) AS "Liczba lingwistow"
FROM 
    Wampiry W
WHERE 
    W.pseudo_wampira IN (
        SELECT 
            JO.pseudo_wampira
        FROM 
            Jezyki_obce_w JO
        GROUP BY 
            JO.pseudo_wampira
        HAVING 
            COUNT(DISTINCT JO.jezyk_obcy) >= 2
    )
GROUP BY 
    W.plec_wampira
ORDER BY 
    W.plec_wampira;
    
--8
--a
SELECT 
    d.ilosc_krwi AS Objetosc,
    d.pseudo_dawcy AS Dawca
FROM 
    Donacje d
WHERE (
    SELECT COUNT(DISTINCT ilosc_krwi)
    FROM Donacje d2
    WHERE d2.ilosc_krwi > d.ilosc_krwi
    ) < 3
ORDER BY ilosc_krwi DESC;

--b
SELECT 
    d.ilosc_krwi AS Objetosc,
    d.pseudo_dawcy AS Dawca
FROM 
    Donacje d
LEFT JOIN 
    Donacje d2 
    ON d.ilosc_krwi < d2.ilosc_krwi
GROUP BY 
    d.ilosc_krwi, d.pseudo_dawcy
HAVING 
    COUNT(DISTINCT d2.ilosc_krwi) < 3
ORDER BY d.ilosc_krwi DESC;


--9
SELECT da.pseudo_dawcy, da.grupa_krwi
FROM Dawcy da
WHERE da.pseudo_dawcy IN 
(
SELECT 
    don.pseudo_dawcy
FROM 
    Donacje don
WHERE 
    don.nr_zlecenia 
    IN(
    SELECT 
        z.nr_zlecenia
    FROM 
        Zlecenia z
    WHERE 
        z.pseudo_wampira 
        IN(
        SELECT 
            W.pseudo_wampira
        FROM 
            Wampiry W
        WHERE 
            W.plec_wampira = 'M'
        AND W.pseudo_wampira 
        IN(
            SELECT 
                jow.pseudo_wampira
            FROM 
                Jezyki_obce_w jow
            WHERE jow.jezyk_obcy = 'polski'
        ))));
--b
SELECT DISTINCT
    d.pseudo_dawcy, d.grupa_krwi, w.pseudo_wampira
FROM 
    Dawcy d
JOIN 
    Donacje don ON d.pseudo_dawcy = don.pseudo_dawcy
JOIN 
    Zlecenia z ON don.nr_zlecenia = z.nr_zlecenia
JOIN 
    Wampiry w ON z.pseudo_wampira = w.pseudo_wampira
JOIN 
    Jezyki_obce_w jow ON w.pseudo_wampira = jow.pseudo_wampira
WHERE 
    w.plec_wampira = 'M'
AND jow.jezyk_obcy = 'polski';

--10
SELECT 
    pseudo_wampira "Wampir",
    EXTRACT(YEAR FROM wampir_w_rodzinie) "Rok wstapienia"
FROM Wampiry 
WHERE EXTRACT(YEAR FROM wampir_w_rodzinie) 
IN (
    SELECT EXTRACT(YEAR FROM wampir_w_rodzinie)
    FROM Wampiry
    GROUP BY EXTRACT(YEAR FROM wampir_w_rodzinie)
    HAVING COUNT(*) > 1
);

--11
SELECT 
    TO_CHAR(EXTRACT(YEAR FROM w.wampir_w_rodzinie)) AS Rok, 
    COUNT(*) AS "Liczba wstapien"
FROM WAMPIRY w
GROUP BY EXTRACT(YEAR FROM w.wampir_w_rodzinie)
HAVING COUNT(*) = (
    SELECT MAX(COUNT(*))
    FROM WAMPIRY w1
    GROUP BY EXTRACT(YEAR FROM w1.wampir_w_rodzinie)
    HAVING COUNT(*) < (
        SELECT AVG(COUNT(EXTRACT(YEAR FROM w1.wampir_w_rodzinie)))
        FROM WAMPIRY w1
        GROUP BY EXTRACT(YEAR FROM w1.wampir_w_rodzinie)
        )
    ) OR COUNT(*) = (
    SELECT MIN(COUNT(*))
    FROM WAMPIRY w1
    GROUP BY EXTRACT(YEAR FROM w1.wampir_w_rodzinie)
    HAVING COUNT(*) > (
        SELECT AVG(COUNT(EXTRACT(YEAR FROM w1.wampir_w_rodzinie)))
        FROM WAMPIRY w1
        GROUP BY EXTRACT(YEAR FROM w1.wampir_w_rodzinie)
        )
    )
UNION
SELECT 
    'średnia' AS ROK, 
    AVG(COUNT(EXTRACT(YEAR FROM w2.wampir_w_rodzinie))) AS Liczba_wstapien
FROM WAMPIRY w2
GROUP BY EXTRACT(YEAR FROM w2.wampir_w_rodzinie)
ORDER BY "Liczba wstapien", Rok;

--12
SELECT 
    d.pseudo_dawcy AS "Dawczyni",
    d.grupa_krwi AS "Grupa krwi",
    (SELECT SUM(don.ilosc_krwi)
    FROM Donacje don
     WHERE 
        don.pseudo_dawcy = d.pseudo_dawcy) AS "W sumie oddala",
    (SELECT 
        AVG(SUM(don1.ilosc_krwi))
     FROM Donacje don1
     JOIN Dawcy d1 
        ON don1.pseudo_dawcy = d1.pseudo_dawcy
     WHERE 
        d1.grupa_krwi = d.grupa_krwi
     GROUP BY d1.pseudo_dawcy) 
        AS "Srednia suma w jej grupie"
FROM Dawcy d
WHERE d.plec_dawcy = 'K';


-- b)
SELECT 
    d.pseudo_dawcy AS "Dawczyni",
    d.grupa_krwi AS "Grupa krwi",
    pel.iloscwsume AS "W sumie oddala",
    srednia_w_grupie.srednia_suma AS "Srednia suma w jej grupie"
FROM Dawcy d
JOIN (
    SELECT 
        dn.pseudo_dawcy,
        SUM(dn.ilosc_krwi) AS iloscwsume
    FROM Donacje dn
    GROUP BY dn.pseudo_dawcy
) pel ON d.pseudo_dawcy = pel.pseudo_dawcy
JOIN (
    SELECT 
        d1.grupa_krwi,
        AVG(SUM(dn1.ilosc_krwi)) OVER (PARTITION BY d1.grupa_krwi) AS srednia_suma
    FROM Donacje dn1
    JOIN Dawcy d1 ON dn1.pseudo_dawcy = d1.pseudo_dawcy
    GROUP BY d1.grupa_krwi
) srednia_w_grupie ON d.grupa_krwi = srednia_w_grupie.grupa_krwi
WHERE d.plec_dawcy = 'K';

--13
SELECT 
    W.pseudo_wampira AS "Wampir", 
    Daw.pseudo_dawcy AS "Zrodlo", 
    SUM(D.ilosc_krwi) AS "Wypil ml"
FROM Wampiry W
JOIN Donacje D ON W.pseudo_wampira = D.pseudo_wampira
JOIN Dawcy Daw ON D.pseudo_dawcy = Daw.pseudo_dawcy
WHERE W.pseudo_wampira NOT IN (SELECT pseudo_wampira FROM Zlecenia)
  AND Daw.plec_dawcy = 'K'
  AND W.plec_wampira = 'M'
  AND D.pseudo_dawcy IN (
      SELECT pseudo_dawcy
      FROM Donacje
      GROUP BY pseudo_dawcy
      HAVING SUM(ilosc_krwi) > 800
  )
GROUP BY W.pseudo_wampira, Daw.pseudo_dawcy;


--14
SELECT pseudo_dawcy, rocznik_dawcy
FROM Dawcy
Where grupa_krwi = '0';

UPDATE Dawcy
SET rocznik_dawcy = rocznik_dawcy + 5
Where grupa_krwi = '0';

SELECT pseudo_dawcy, rocznik_dawcy
FROM Dawcy
Where grupa_krwi = '0';

ROLLBACK;

--sprawdzenie
SELECT pseudo_dawcy, rocznik_dawcy
FROM Dawcy
Where grupa_krwi = '0';

--15
SELECT w.pseudo_wampira AS "Pseudo wampira", NVL(w.pseudo_szefa, ' ') AS "Pseudo szefa",
       NVL(TO_CHAR(w1.wampir_w_rodzinie, 'DD.MM.YYYY'), ' ') AS "W Rodzinie s", NVL(w1.pseudo_szefa, ' ') AS "Pseudo szefa szefa",
       NVL(TO_CHAR(w2.wampir_w_rodzinie, 'DD.MM.YYYY'), ' ') AS "W rodzinie ss"
From Wampiry w
LEFT JOIN 
    Wampiry w1 ON w.pseudo_szefa = w1.pseudo_wampira
LEFT JOIN 
    Wampiry w2 ON w1.pseudo_szefa = w2.pseudo_wampira
WHERE w.plec_wampira = 'M'
ORDER BY "Pseudo wampira", 
    "W Rodzinie s"
;

--16

SELECT 
CASE 
    WHEN W.plec_wampira = 'K' THEN 'Wampirki'
    WHEN W.plec_wampira = 'M' THEN 'Wampiry'
    END AS "Plec podwladnych",
    SUM(CASE WHEN W.pseudo_szefa = 'Drakula' THEN d.ilosc_krwi ELSE 0 END) AS "Pod Drakula",
    SUM(CASE WHEN W.pseudo_szefa = 'Opoj' THEN d.ilosc_krwi ELSE 0 END) AS "Pod Opojem",
    SUM(CASE WHEN W.pseudo_szefa = 'Wicek' THEN d.ilosc_krwi ELSE 0 END) AS "Pod Wickiem"
FROM 
    Wampiry W
JOIN 
    Donacje d ON w.pseudo_wampira = d.pseudo_wampira
WHERE 
    w.pseudo_szefa IS NOT NULL
GROUP BY 
    w.plec_wampira;
