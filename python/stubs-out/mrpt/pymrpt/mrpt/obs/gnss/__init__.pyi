from typing import Any, ClassVar, List

from typing import overload
import mrpt.pymrpt.mrpt.math
import mrpt.pymrpt.mrpt.serialization
import mrpt.pymrpt.std.chrono
NMEA_GGA: gnss_message_type_t
NMEA_GLL: gnss_message_type_t
NMEA_GSA: gnss_message_type_t
NMEA_GSV: gnss_message_type_t
NMEA_MSS: gnss_message_type_t
NMEA_RMC: gnss_message_type_t
NMEA_VTG: gnss_message_type_t
NMEA_ZDA: gnss_message_type_t
NV_OEM6_ALIGNBSLNENU: gnss_message_type_t
NV_OEM6_ALIGNBSLNXYZ: gnss_message_type_t
NV_OEM6_ALIGNDOP: gnss_message_type_t
NV_OEM6_BESTPOS: gnss_message_type_t
NV_OEM6_BESTSATS: gnss_message_type_t
NV_OEM6_BESTUTM: gnss_message_type_t
NV_OEM6_BESTVEL: gnss_message_type_t
NV_OEM6_BESTXYZ: gnss_message_type_t
NV_OEM6_CLOCKSTEERING: gnss_message_type_t
NV_OEM6_GENERIC_FRAME: gnss_message_type_t
NV_OEM6_GENERIC_SHORT_FRAME: gnss_message_type_t
NV_OEM6_GPGGA: gnss_message_type_t
NV_OEM6_GPGGARTK: gnss_message_type_t
NV_OEM6_GPGLL: gnss_message_type_t
NV_OEM6_GPGSA: gnss_message_type_t
NV_OEM6_GPGSV: gnss_message_type_t
NV_OEM6_GPHDT: gnss_message_type_t
NV_OEM6_GPRMC: gnss_message_type_t
NV_OEM6_GPVTG: gnss_message_type_t
NV_OEM6_GPZDA: gnss_message_type_t
NV_OEM6_INSATTS: gnss_message_type_t
NV_OEM6_INSCOVS: gnss_message_type_t
NV_OEM6_INSPVAS: gnss_message_type_t
NV_OEM6_INSVELS: gnss_message_type_t
NV_OEM6_IONUTC: gnss_message_type_t
NV_OEM6_MARK2POS: gnss_message_type_t
NV_OEM6_MARK2TIME: gnss_message_type_t
NV_OEM6_MARKPOS: gnss_message_type_t
NV_OEM6_MARKTIME: gnss_message_type_t
NV_OEM6_MSG2ENUM: gnss_message_type_t
NV_OEM6_PPPPOS: gnss_message_type_t
NV_OEM6_RANGECMP: gnss_message_type_t
NV_OEM6_RAWEPHEM: gnss_message_type_t
NV_OEM6_RAWIMUS: gnss_message_type_t
NV_OEM6_RXSTATUS: gnss_message_type_t
NV_OEM6_VERSION: gnss_message_type_t
TOPCON_PZS: gnss_message_type_t
TOPCON_SATS: gnss_message_type_t

class Message_NMEA_GGA(gnss_message):
    class content_t:
        HDOP: float
        UTCTime: UTC_time
        altitude_meters: float
        corrected_orthometric_altitude: float
        fix_quality: int
        geoidal_distance: float
        latitude_degrees: float
        longitude_degrees: float
        orthometric_altitude: float
        satellitesUsed: int
        thereis_HDOP: bool
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Message_NMEA_GGA.content_t) -> None: ...
        def assign(self) -> Message_NMEA_GGA.content_t: ...
    fields: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NMEA_GGA) -> None: ...
    @overload
    def __init__(self, arg0: Message_NMEA_GGA) -> None: ...
    def assign(self) -> Message_NMEA_GGA: ...

class Message_NMEA_GLL(gnss_message):
    class content_t:
        UTCTime: UTC_time
        latitude_degrees: float
        longitude_degrees: float
        validity_char: int
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Message_NMEA_GLL.content_t) -> None: ...
        def assign(self) -> Message_NMEA_GLL.content_t: ...
    fields: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NMEA_GLL) -> None: ...
    @overload
    def __init__(self, arg0: Message_NMEA_GLL) -> None: ...
    def assign(self) -> Message_NMEA_GLL: ...

class Message_NMEA_GSA(gnss_message):
    class content_t:
        HDOP: float
        PDOP: float
        VDOP: float
        auto_selection_fix: str
        fix_2D_3D: str
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Message_NMEA_GSA.content_t) -> None: ...
        def assign(self) -> Message_NMEA_GSA.content_t: ...
    fields: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NMEA_GSA) -> None: ...
    @overload
    def __init__(self, arg0: Message_NMEA_GSA) -> None: ...
    def assign(self) -> Message_NMEA_GSA: ...

class Message_NMEA_RMC(gnss_message):
    class content_t:
        UTCTime: UTC_time
        date_day: int
        date_month: int
        date_year: int
        direction_degrees: float
        latitude_degrees: float
        longitude_degrees: float
        magnetic_dir: float
        positioning_mode: str
        speed_knots: float
        validity_char: int
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Message_NMEA_RMC.content_t) -> None: ...
        def assign(self) -> Message_NMEA_RMC.content_t: ...
    fields: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NMEA_RMC) -> None: ...
    @overload
    def __init__(self, arg0: Message_NMEA_RMC) -> None: ...
    def assign(self) -> Message_NMEA_RMC: ...
    def getDateAsTimestamp(self) -> mrpt.pymrpt.std.chrono.time_point_mrpt_Clock_std_chrono_duration_long_std_ratio_1_10000000_t: ...

class Message_NMEA_VTG(gnss_message):
    class content_t:
        ground_speed_kmh: float
        ground_speed_knots: float
        magnetic_track: float
        true_track: float
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Message_NMEA_VTG.content_t) -> None: ...
        def assign(self) -> Message_NMEA_VTG.content_t: ...
    fields: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NMEA_VTG) -> None: ...
    @overload
    def __init__(self, arg0: Message_NMEA_VTG) -> None: ...
    def assign(self) -> Message_NMEA_VTG: ...

class Message_NMEA_ZDA(gnss_message):
    class content_t:
        UTCTime: UTC_time
        date_day: int
        date_month: int
        date_year: int
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Message_NMEA_ZDA.content_t) -> None: ...
        def assign(self) -> Message_NMEA_ZDA.content_t: ...
    fields: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NMEA_ZDA) -> None: ...
    @overload
    def __init__(self, arg0: Message_NMEA_ZDA) -> None: ...
    def assign(self) -> Message_NMEA_ZDA: ...
    def getDateAsTimestamp(self) -> mrpt.pymrpt.std.chrono.time_point_mrpt_Clock_std_chrono_duration_long_std_ratio_1_10000000_t: ...
    def getDateTimeAsTimestamp(self) -> mrpt.pymrpt.std.chrono.time_point_mrpt_Clock_std_chrono_duration_long_std_ratio_1_10000000_t: ...

class Message_NV_OEM6_BESTPOS(gnss_message):
    class content_t:
        crc: int
        datum_id: int
        diff_age: float
        ext_sol_stat: int
        galileo_beidou_mask: int
        gps_glonass_mask: int
        header: nv_oem6_header_t
        hgt: float
        hgt_sigma: float
        lat: float
        lat_sigma: float
        lon: float
        lon_sigma: float
        num_sats_sol: int
        num_sats_sol_L1: int
        num_sats_sol_multi: int
        num_sats_tracked: int
        position_type: nv_oem6_position_type.nv_position_type_t
        reserved: int
        sol_age: float
        solution_stat: nv_oem6_solution_status.nv_solution_status_t
        undulation: float
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Message_NV_OEM6_BESTPOS.content_t) -> None: ...
        def assign(self) -> Message_NV_OEM6_BESTPOS.content_t: ...
    fields: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_BESTPOS) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_BESTPOS) -> None: ...
    def assign(self) -> Message_NV_OEM6_BESTPOS: ...
    @overload
    def fixEndianness(self) -> None: ...
    @overload
    def fixEndianness() -> void: ...

class Message_NV_OEM6_GENERIC_FRAME(gnss_message):
    header: nv_oem6_header_t
    msg_body: List[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_GENERIC_FRAME) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_GENERIC_FRAME) -> None: ...
    def assign(self) -> Message_NV_OEM6_GENERIC_FRAME: ...
    @overload
    def fixEndianness(self) -> None: ...
    @overload
    def fixEndianness() -> void: ...

class Message_NV_OEM6_GENERIC_SHORT_FRAME(gnss_message):
    header: nv_oem6_short_header_t
    msg_body: List[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_GENERIC_SHORT_FRAME) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_GENERIC_SHORT_FRAME) -> None: ...
    def assign(self) -> Message_NV_OEM6_GENERIC_SHORT_FRAME: ...
    @overload
    def fixEndianness(self) -> None: ...
    @overload
    def fixEndianness() -> void: ...

class Message_NV_OEM6_INSCOVS(gnss_message):
    class content_t:
        crc: int
        header: nv_oem6_short_header_t
        seconds_in_week: float
        week: int
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Message_NV_OEM6_INSCOVS.content_t) -> None: ...
        def assign(self) -> Message_NV_OEM6_INSCOVS.content_t: ...
    fields: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_INSCOVS) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_INSCOVS) -> None: ...
    def assign(self) -> Message_NV_OEM6_INSCOVS: ...
    @overload
    def fixEndianness(self) -> None: ...
    @overload
    def fixEndianness() -> void: ...

class Message_NV_OEM6_INSPVAS(gnss_message):
    class content_t:
        azimuth: float
        crc: int
        header: nv_oem6_short_header_t
        hgt: float
        ins_status: nv_oem6_ins_status_type.nv_ins_status_type_t
        lat: float
        lon: float
        pitch: float
        roll: float
        seconds_in_week: float
        vel_east: float
        vel_north: float
        vel_up: float
        week: int
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Message_NV_OEM6_INSPVAS.content_t) -> None: ...
        def assign(self) -> Message_NV_OEM6_INSPVAS.content_t: ...
    fields: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_INSPVAS) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_INSPVAS) -> None: ...
    def assign(self) -> Message_NV_OEM6_INSPVAS: ...
    @overload
    def fixEndianness(self) -> None: ...
    @overload
    def fixEndianness() -> void: ...

class Message_NV_OEM6_IONUTC(gnss_message):
    class content_t:
        A0: float
        A1: float
        a0: float
        a1: float
        a2: float
        a3: float
        b0: float
        b1: float
        b2: float
        b3: float
        crc: int
        deltat_ls: int
        deltat_lsf: int
        dn: int
        header: nv_oem6_header_t
        reserved: int
        tot: int
        utc_wn: int
        wn_lsf: int
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Message_NV_OEM6_IONUTC.content_t) -> None: ...
        def assign(self) -> Message_NV_OEM6_IONUTC.content_t: ...
    fields: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_IONUTC) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_IONUTC) -> None: ...
    def assign(self) -> Message_NV_OEM6_IONUTC: ...
    @overload
    def fixEndianness(self) -> None: ...
    @overload
    def fixEndianness() -> void: ...

class Message_NV_OEM6_MARK2TIME(gnss_message):
    class content_t:
        clock_offset: float
        clock_offset_std: float
        clock_status: int
        crc: int
        header: nv_oem6_header_t
        utc_offset: float
        week: int
        week_seconds: float
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Message_NV_OEM6_MARK2TIME.content_t) -> None: ...
        def assign(self) -> Message_NV_OEM6_MARK2TIME.content_t: ...
    fields: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_MARK2TIME) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_MARK2TIME) -> None: ...
    def assign(self) -> Message_NV_OEM6_MARK2TIME: ...
    @overload
    def fixEndianness(self) -> None: ...
    @overload
    def fixEndianness() -> void: ...

class Message_NV_OEM6_MARKPOS(gnss_message):
    class content_t:
        crc: int
        datum_id: int
        diff_age: float
        ext_sol_stat: int
        galileo_beidou_mask: int
        gps_glonass_mask: int
        header: nv_oem6_header_t
        hgt: float
        hgt_sigma: float
        lat: float
        lat_sigma: float
        lon: float
        lon_sigma: float
        num_sats_sol: int
        num_sats_sol_L1: int
        num_sats_sol_multi: int
        num_sats_tracked: int
        position_type: nv_oem6_position_type.nv_position_type_t
        reserved: int
        sol_age: float
        solution_stat: nv_oem6_solution_status.nv_solution_status_t
        undulation: float
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Message_NV_OEM6_MARKPOS.content_t) -> None: ...
        def assign(self) -> Message_NV_OEM6_MARKPOS.content_t: ...
    fields: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_MARKPOS) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_MARKPOS) -> None: ...
    def assign(self) -> Message_NV_OEM6_MARKPOS: ...
    @overload
    def fixEndianness(self) -> None: ...
    @overload
    def fixEndianness() -> void: ...

class Message_NV_OEM6_MARKTIME(gnss_message):
    class content_t:
        clock_offset: float
        clock_offset_std: float
        clock_status: int
        crc: int
        header: nv_oem6_header_t
        utc_offset: float
        week: int
        week_seconds: float
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Message_NV_OEM6_MARKTIME.content_t) -> None: ...
        def assign(self) -> Message_NV_OEM6_MARKTIME.content_t: ...
    fields: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_MARKTIME) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_MARKTIME) -> None: ...
    def assign(self) -> Message_NV_OEM6_MARKTIME: ...
    @overload
    def fixEndianness(self) -> None: ...
    @overload
    def fixEndianness() -> void: ...

class Message_NV_OEM6_RANGECMP(gnss_message):
    class TCompressedRangeLog:
        def __init__(self) -> None: ...
    crc: int
    header: nv_oem6_header_t
    num_obs: int
    obs_data: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_RANGECMP) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_RANGECMP) -> None: ...
    def assign(self) -> Message_NV_OEM6_RANGECMP: ...

class Message_NV_OEM6_RAWEPHEM(gnss_message):
    class content_t:
        crc: int
        header: nv_oem6_header_t
        ref_secs: int
        ref_week: int
        sat_prn: int
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Message_NV_OEM6_RAWEPHEM.content_t) -> None: ...
        def assign(self) -> Message_NV_OEM6_RAWEPHEM.content_t: ...
    fields: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_RAWEPHEM) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_RAWEPHEM) -> None: ...
    def assign(self) -> Message_NV_OEM6_RAWEPHEM: ...
    @overload
    def fixEndianness(self) -> None: ...
    @overload
    def fixEndianness() -> void: ...

class Message_NV_OEM6_RAWIMUS(gnss_message):
    class content_t:
        accel_x: int
        accel_y_neg: int
        accel_z: int
        crc: int
        gyro_x: int
        gyro_y_neg: int
        gyro_z: int
        header: nv_oem6_short_header_t
        imu_status: int
        week: int
        week_seconds: float
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Message_NV_OEM6_RAWIMUS.content_t) -> None: ...
        def assign(self) -> Message_NV_OEM6_RAWIMUS.content_t: ...
    fields: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_RAWIMUS) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_RAWIMUS) -> None: ...
    def assign(self) -> Message_NV_OEM6_RAWIMUS: ...
    @overload
    def fixEndianness(self) -> None: ...
    @overload
    def fixEndianness() -> void: ...

class Message_NV_OEM6_RXSTATUS(gnss_message):
    class content_t:
        aux1stat: int
        aux1stat_clear: int
        aux1stat_pri: int
        aux1stat_set: int
        aux2stat: int
        aux2stat_clear: int
        aux2stat_pri: int
        aux2stat_set: int
        aux3stat: int
        aux3stat_clear: int
        aux3stat_pri: int
        aux3stat_set: int
        crc: int
        error: int
        header: nv_oem6_header_t
        num_stats: int
        rxstat: int
        rxstat_clear: int
        rxstat_pri: int
        rxstat_set: int
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Message_NV_OEM6_RXSTATUS.content_t) -> None: ...
        def assign(self) -> Message_NV_OEM6_RXSTATUS.content_t: ...
    fields: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_RXSTATUS) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_RXSTATUS) -> None: ...
    def assign(self) -> Message_NV_OEM6_RXSTATUS: ...
    @overload
    def fixEndianness(self) -> None: ...
    @overload
    def fixEndianness() -> void: ...

class Message_NV_OEM6_VERSION(gnss_message):
    class TComponentVersion:
        type: int
        def __init__(self) -> None: ...
    components: Any
    crc: int
    header: nv_oem6_header_t
    num_comps: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_VERSION) -> None: ...
    @overload
    def __init__(self, arg0: Message_NV_OEM6_VERSION) -> None: ...
    def assign(self) -> Message_NV_OEM6_VERSION: ...
    @overload
    def fixEndianness(self) -> None: ...
    @overload
    def fixEndianness() -> void: ...

class Message_TOPCON_PZS(gnss_message):
    Fix: int
    PSigma: float
    RTK_height_meters: float
    RXBattery: int
    TXBattery: int
    angle_transmitter: float
    cartesian_vx: float
    cartesian_vy: float
    cartesian_vz: float
    cartesian_x: float
    cartesian_y: float
    cartesian_z: float
    error: int
    hasCartesianPosVel: bool
    hasPosCov: bool
    hasStats: bool
    hasVelCov: bool
    height_meters: float
    latitude_degrees: float
    longitude_degrees: float
    nId: int
    pos_covariance: mrpt.pymrpt.mrpt.math.CMatrixFixed_float_4UL_4UL_t
    stats_GLONASS_sats_used: int
    stats_GPS_sats_used: int
    stats_rtk_fix_progress: int
    vel_covariance: mrpt.pymrpt.mrpt.math.CMatrixFixed_float_4UL_4UL_t
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_TOPCON_PZS) -> None: ...
    @overload
    def __init__(self, arg0: Message_TOPCON_PZS) -> None: ...
    def assign(self) -> Message_TOPCON_PZS: ...

class Message_TOPCON_SATS(gnss_message):
    AZs: List[int]
    ELs: List[int]
    USIs: List[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Message_TOPCON_SATS) -> None: ...
    @overload
    def __init__(self, arg0: Message_TOPCON_SATS) -> None: ...
    def assign(self) -> Message_TOPCON_SATS: ...

class UTC_time:
    __hash__: ClassVar[None] = ...
    hour: int
    minute: int
    sec: float
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: UTC_time) -> None: ...
    def assign(self) -> UTC_time: ...
    def getAsTimestamp(self, date: mrpt.pymrpt.std.chrono.time_point_mrpt_Clock_std_chrono_duration_long_std_ratio_1_10000000_t) -> mrpt.pymrpt.std.chrono.time_point_mrpt_Clock_std_chrono_duration_long_std_ratio_1_10000000_t: ...
    @overload
    def readFromStream(self, in: mrpt.pymrpt.mrpt.serialization.CArchive) -> None: ...
    @overload
    def readFromStream(classmrpt) -> void: ...
    @overload
    def writeToStream(self, out: mrpt.pymrpt.mrpt.serialization.CArchive) -> None: ...
    @overload
    def writeToStream(classmrpt) -> void: ...
    def __eq__(self, o: UTC_time) -> bool: ...
    def __ne__(self, o: UTC_time) -> bool: ...

class gnss_message:
    message_type: gnss_message_type_t
    def __init__(self, *args, **kwargs) -> None: ...
    def Factory(self, *args, **kwargs) -> Any: ...
    def FactoryKnowsMsgType(self, *args, **kwargs) -> Any: ...
    def assign(self) -> gnss_message: ...
    @overload
    def fixEndianness(self) -> None: ...
    @overload
    def fixEndianness() -> void: ...
    def getMessageTypeAsString(self) -> str: ...
    @overload
    def isOfType(self, type_id: gnss_message_type_t) -> bool: ...
    @overload
    def isOfType(constenummrpt) -> bool: ...
    def readAndBuildFromStream(self, *args, **kwargs) -> Any: ...
    @overload
    def readFromStream(self, in: mrpt.pymrpt.mrpt.serialization.CArchive) -> None: ...
    @overload
    def readFromStream(classmrpt) -> void: ...
    @overload
    def writeToStream(self, out: mrpt.pymrpt.mrpt.serialization.CArchive) -> None: ...
    @overload
    def writeToStream(classmrpt) -> void: ...

class gnss_message_ptr:
    __hash__: ClassVar[None] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: gnss_message_ptr) -> None: ...
    @overload
    def __init__(self, p: gnss_message) -> None: ...
    def arrow(self) -> gnss_message: ...
    def assign(self, o: gnss_message_ptr) -> gnss_message_ptr: ...
    def get(self) -> gnss_message: ...
    @overload
    def set(self, p: gnss_message) -> None: ...
    @overload
    def set(structmrpt) -> void: ...
    @overload
    def __eq__(self, o: gnss_message) -> bool: ...
    @overload
    def __eq__(self, o: gnss_message_ptr) -> bool: ...
    @overload
    def __ne__(self, o: gnss_message) -> bool: ...
    @overload
    def __ne__(self, o: gnss_message_ptr) -> bool: ...

class gnss_message_type_t:
    __doc__: ClassVar[str] = ...  # read-only
    __members__: ClassVar[dict] = ...  # read-only
    NMEA_GGA: ClassVar[gnss_message_type_t] = ...
    NMEA_GLL: ClassVar[gnss_message_type_t] = ...
    NMEA_GSA: ClassVar[gnss_message_type_t] = ...
    NMEA_GSV: ClassVar[gnss_message_type_t] = ...
    NMEA_MSS: ClassVar[gnss_message_type_t] = ...
    NMEA_RMC: ClassVar[gnss_message_type_t] = ...
    NMEA_VTG: ClassVar[gnss_message_type_t] = ...
    NMEA_ZDA: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_ALIGNBSLNENU: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_ALIGNBSLNXYZ: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_ALIGNDOP: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_BESTPOS: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_BESTSATS: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_BESTUTM: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_BESTVEL: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_BESTXYZ: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_CLOCKSTEERING: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_GENERIC_FRAME: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_GENERIC_SHORT_FRAME: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_GPGGA: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_GPGGARTK: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_GPGLL: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_GPGSA: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_GPGSV: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_GPHDT: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_GPRMC: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_GPVTG: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_GPZDA: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_INSATTS: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_INSCOVS: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_INSPVAS: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_INSVELS: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_IONUTC: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_MARK2POS: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_MARK2TIME: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_MARKPOS: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_MARKTIME: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_MSG2ENUM: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_PPPPOS: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_RANGECMP: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_RAWEPHEM: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_RAWIMUS: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_RXSTATUS: ClassVar[gnss_message_type_t] = ...
    NV_OEM6_VERSION: ClassVar[gnss_message_type_t] = ...
    TOPCON_PZS: ClassVar[gnss_message_type_t] = ...
    TOPCON_SATS: ClassVar[gnss_message_type_t] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __and__(self, other: object) -> object: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __invert__(self) -> object: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __or__(self, other: object) -> object: ...
    def __rand__(self, other: object) -> object: ...
    def __ror__(self, other: object) -> object: ...
    def __rxor__(self, other: object) -> object: ...
    def __setstate__(self, state: int) -> None: ...
    def __xor__(self, other: object) -> object: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class nv_oem6_header_t:
    hdr_len: int
    idle_percent: int
    ms_in_week: int
    msg_id: int
    msg_len: int
    msg_type: int
    port_addr: int
    receiver_status: int
    receiver_sw_version: int
    reserved: int
    seq_number: int
    time_status: int
    week: int
    @overload
    def __init__(self, arg0: nv_oem6_header_t) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def assign(self) -> nv_oem6_header_t: ...
    @overload
    def fixEndianness(self) -> None: ...
    @overload
    def fixEndianness() -> void: ...

class nv_oem6_short_header_t:
    ms_in_week: int
    msg_id: int
    msg_len: int
    week: int
    @overload
    def __init__(self, arg0: nv_oem6_short_header_t) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def assign(self) -> nv_oem6_short_header_t: ...
    @overload
    def fixEndianness(self) -> None: ...
    @overload
    def fixEndianness() -> void: ...