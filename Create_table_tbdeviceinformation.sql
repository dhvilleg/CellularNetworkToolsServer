CREATE TABLE IF NOT EXISTS `tbdeviceinformation` (
  `deviceUUID` VARCHAR(37) NOT NULL COLLATE 'utf8_general_ci',
  `deviceModel` VARCHAR(10) NOT NULL COLLATE 'utf8_general_ci',
  `deviceOS` VARCHAR(10) NOT NULL COLLATE 'utf8_general_ci',
  `osVersion` VARCHAR(10) NOT NULL COLLATE 'utf8_general_ci',
  `isDualSim` INT(11) NOT NULL,
  `fieldIsRegistered` INT(11) NOT NULL,

  PRIMARY KEY (`deviceUUID`) USING BTREE) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabla para almacenar informción de dispositivo capturada de aplicacion arcotel';
