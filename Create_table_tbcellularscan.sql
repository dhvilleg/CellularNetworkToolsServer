CREATE TABLE IF NOT EXISTS `tbcellularscan` (
  `scanid` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` VARCHAR(20) NOT NULL,
  `deviceUUID` VARCHAR(37) NOT NULL,
  `ratingCounter` VARCHAR(5) NOT NULL,
  `simNumberID` VARCHAR(11) NOT NULL,
  `countryISO` VARCHAR(3) NOT NULL,
  `phoneOperatorId` VARCHAR(20) NOT NULL,
  `simOperatorId` VARCHAR(8) NOT NULL,
  `operatorMcc` VARCHAR(5) NOT NULL,
  `operatorMnc` VARCHAR(5) NOT NULL,
  `devManufacturer` VARCHAR(20) NOT NULL,
  `devModel` VARCHAR(20) NOT NULL,
  `isConected` VARCHAR(15) NOT NULL,
  `phoneNetStandard` VARCHAR(5) NOT NULL,
  `phoneNetTechnology` VARCHAR(12) NOT NULL,
  `internetConNetwork` VARCHAR(7) NOT NULL,
  `latitude` VARCHAR(15) NOT NULL,
  `longitude` VARCHAR(15) NOT NULL,
  `pingTimeMilis` VARCHAR(15) NOT NULL,
  `downloadSpeed` VARCHAR(15) NOT NULL,
  `uploadSpeed` VARCHAR(15) NOT NULL,
  `ipPublicAddr` VARCHAR(15) NOT NULL,
  `internetISP` VARCHAR(15) NOT NULL,
  `phoneSignalStrength` VARCHAR(12) NOT NULL,
  `phoneAsuStrength` VARCHAR(12) NOT NULL,
  `phoneSignalLevel` VARCHAR(12) NOT NULL,
  `signalQuality` VARCHAR(10) NOT NULL,
  `fieldIsRegistered` INT(2) NOT NULL,
  `phoneRsrpStrength` VARCHAR(12) NOT NULL,
  `phoneRssnrStrength` VARCHAR(15) NOT NULL,
  `phoneTimingAdvance` VARCHAR(12) NOT NULL,
  `phoneCqiStrength` VARCHAR(12) NOT NULL,
  `phoneRsrqStrength` VARCHAR(12) NOT NULL,
  `cellLtePci` VARCHAR(12) NOT NULL,
  `cellLteCid` VARCHAR(12) NOT NULL,
  `cellLteTac` VARCHAR(12) NOT NULL,
  `cellLteeNodeB` VARCHAR(12) NOT NULL,
  `cellLteEarfcn` VARCHAR(12) NOT NULL,
  `cellBslat` VARCHAR(12) NOT NULL,
  `cellBslon` VARCHAR(12) NOT NULL,
  `cellSid` VARCHAR(12) NOT NULL,
  `cellNid` VARCHAR(12) NOT NULL,
  `cellBid` VARCHAR(12) NOT NULL,
  `cellWcdmaLac` VARCHAR(12) NOT NULL,
  `cellWcdmaUcid` VARCHAR(12) NOT NULL,
  `cellWcdmaUarfcn` VARCHAR(12) NOT NULL,
  `cellWcdmaPsc` VARCHAR(12) NOT NULL,
  `cellWcdmaCid` VARCHAR(12) NOT NULL,
  `cellWcdmaRnc` VARCHAR(12) NOT NULL,
  `cellGsmArcfn` VARCHAR(12) NOT NULL,
  `cellGsmLac` VARCHAR(12) NOT NULL,
  `cellGsmCid` VARCHAR(12) NOT NULL,
  PRIMARY KEY (`scanid`) USING BTREE)
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = utf8
  COMMENT = 'Tabla para almacenar informción de la aplicación android'
