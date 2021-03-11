-- phpMyAdmin SQL Dump
-- version 3.5.4
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2018 年 06 月 21 日 16:55
-- 服务器版本: 5.6.39
-- PHP 版本: 5.3.10-1ubuntu3.26

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `codeManageAndShare`
--

-- --------------------------------------------------------

--
-- 表的结构 `app_codeManage_codediscuss`
--

CREATE TABLE IF NOT EXISTS `app_codeManage_codediscuss` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codeDiscussSecondNumber` varchar(20) NOT NULL,
  `codeDiscussUserCreateID` varchar(20) NOT NULL,
  `codeDiscussUserReplyID` varchar(20) NOT NULL,
  `codeDiscussCreateDataTime` datetime NOT NULL,
  `codeDiscussIsDelete` tinyint(1) NOT NULL,
  `codeDiscussContent` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=13 ;

--
-- 转存表中的数据 `app_codeManage_codediscuss`
--

INSERT INTO `app_codeManage_codediscuss` (`id`, `codeDiscussSecondNumber`, `codeDiscussUserCreateID`, `codeDiscussUserReplyID`, `codeDiscussCreateDataTime`, `codeDiscussIsDelete`, `codeDiscussContent`) VALUES
(1, '20180511184531_oKP', '1', '0', '2018-05-19 13:07:58', 0, 'Very Good'),
(2, '20180511184531_oKP', '2', '1', '2018-05-19 14:15:42', 0, '不错不错'),
(3, '20180511184531_oKP', '1', '0', '2018-05-19 14:46:35', 0, '大时代'),
(4, '20180511184531_oKP', '1', '1', '2018-05-19 14:46:47', 0, '哈哈'),
(5, '20180511184531_oKP', '1', '2', '2018-05-19 14:48:40', 0, '这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容这是评论的内容'),
(7, '20180511184531_oKP', '1', '0', '2018-05-19 14:52:12', 0, 'aaa'),
(8, '20180507131912_i6d', '1', '0', '2018-05-19 18:08:46', 0, '有点意思'),
(9, '20180511184531_oKP', '3', '0', '2018-05-19 19:03:36', 0, '苏打水'),
(10, '20180511184531_oKP', '1', '3', '2018-05-19 19:15:04', 0, '对方哈伦裤阶段'),
(11, '20180511184725_oWO', '1', '0', '2018-05-25 21:13:08', 0, '这是一个问题'),
(12, '20180511184725_oWO', '1', '1', '2018-05-25 21:18:00', 0, '这个问题提的非常棒啊！');

-- --------------------------------------------------------

--
-- 表的结构 `app_codeManage_codelanguage`
--

CREATE TABLE IF NOT EXISTS `app_codeManage_codelanguage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codeLanguageType` varchar(20) NOT NULL,
  `codeLanguageTime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=13 ;

--
-- 转存表中的数据 `app_codeManage_codelanguage`
--

INSERT INTO `app_codeManage_codelanguage` (`id`, `codeLanguageType`, `codeLanguageTime`) VALUES
(1, 'Java', '2018-04-28 17:36:05'),
(2, 'C++', '2018-04-28 17:41:14'),
(3, 'C', '2018-05-05 20:50:51'),
(4, 'Objective-C', '2018-05-05 20:50:51'),
(5, 'C#', '2018-05-05 20:50:51'),
(6, 'PHP', '2018-05-05 20:50:51'),
(7, 'Basic', '2018-05-05 20:50:51'),
(8, 'Python', '2018-05-05 20:52:18'),
(9, 'JavaScript', '2018-05-05 20:52:18'),
(10, 'Perl', '2018-05-05 20:52:18'),
(11, 'Ruby', '2018-05-05 20:52:18'),
(12, 'Lisp', '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- 表的结构 `app_codeManage_codemanage`
--

CREATE TABLE IF NOT EXISTS `app_codeManage_codemanage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codeManageFirstNumber` varchar(20) NOT NULL,
  `codeManageSecondNumber` varchar(20) NOT NULL,
  `codeManageCodeName` varchar(30) NOT NULL,
  `codeManageCodeAuthor` varchar(20) NOT NULL,
  `codeManageIsShare` tinyint(1) NOT NULL,
  `codeManageLanguage` varchar(20) NOT NULL,
  `codeManageSearchTimes` int(11) NOT NULL,
  `codeManageCheckTimes` int(11) NOT NULL,
  `codeManageDownloadTimes` int(11) NOT NULL,
  `codeManageCodeExplain` longtext NOT NULL,
  `codeManageSavePosition` varchar(254) NOT NULL,
  `codeManageUploadTime` datetime NOT NULL,
  `codeManageMainFlag` tinyint(1) NOT NULL,
  `codeManageIsDelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=51 ;

--
-- 转存表中的数据 `app_codeManage_codemanage`
--

INSERT INTO `app_codeManage_codemanage` (`id`, `codeManageFirstNumber`, `codeManageSecondNumber`, `codeManageCodeName`, `codeManageCodeAuthor`, `codeManageIsShare`, `codeManageLanguage`, `codeManageSearchTimes`, `codeManageCheckTimes`, `codeManageDownloadTimes`, `codeManageCodeExplain`, `codeManageSavePosition`, `codeManageUploadTime`, `codeManageMainFlag`, `codeManageIsDelete`) VALUES
(24, '20180501224917_E', '20180501224917_psQ', '大夫敢死队', '1', 1, '1', 0, 12, 0, '打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的打扫打扫打扫的', '/static/codeSavePosition/20180501224917_E/20180501224917_psQ/codeManageAndShare.zip', '2018-05-01 22:49:17', 1, 0),
(25, '20180502161601_u', '20180502161601_ISn', '三Q软件', '1', 1, '1', 0, 3, 0, '这是为了测试的第一个如那件', '/static/codeSavePosition/20180502161601_u/20180502161601_ISn/qqq.zip', '2018-05-02 16:16:01', 1, 0),
(26, '20180502161746_7', '20180502161746_jiS', '四Q软件', '1', 1, '1', 0, 8, 0, '这是为了测试的第四个软大事', '/static/codeSavePosition/20180502161746_7/20180502161746_jiS/qqq.zip', '2018-05-02 16:17:46', 1, 0),
(28, '20180502162755_x', '20180502162755_eAl', '奴家软件', '1', 1, '1', 0, 20, 0, 'bijkbhiouiuniuiougy8yg8uy', '/static/codeSavePosition/20180502162755_x/20180502162755_eAl/codeManageAndShare.zip', '2018-05-02 16:27:55', 1, 0),
(29, '20180502163038_l', '20180502163038_aAG', '恶法软件', '1', 1, '1', 0, 26, 0, '法尔啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊', '/static/codeSavePosition/20180502163038_l/20180502163038_aAG/codeManageAndShare.zip', '2018-05-02 16:30:38', 1, 0),
(31, '20180505110501_5', '20180505191854_WLB', '地衣软件', '1', 1, '1', 0, 6, 0, '这是第二个版本', '/static/codeSavePosition/20180505110501_5/20180505191854_WLB/codeManageAndShare.zip', '2018-05-05 19:18:54', 0, 0),
(32, '20180505110501_5', '20180505194335_c16', '地衣软件', '1', 1, '1', 0, 186, 0, '第三个版本', '/static/codeSavePosition/20180505110501_5/20180505194335_c16/codeManageAndShare.zip', '2018-05-05 19:43:35', 0, 1),
(33, '20180505195015_U', '20180505195015_8MP', 'login登录模块', '1', 1, '1', 0, 10, 0, '这是登录模块', '/static/codeSavePosition/20180505195015_U/20180505195015_8MP/login.zip', '2018-05-05 19:50:15', 1, 0),
(34, '20180505195015_U', '20180505195146_5Xf', 'login登录模块', '1', 1, '1', 0, 8, 0, '这是第二个版本', '/static/codeSavePosition/20180505195015_U/20180505195146_5Xf/login.zip', '2018-05-05 19:51:46', 0, 0),
(35, '20180505195015_U', '20180506111635_Sj6', 'login登录模块', '1', 1, '1', 0, 2, 0, '第三个版本', '/static/codeSavePosition/20180505195015_U/20180506111635_Sj6/login.zip', '2018-05-06 11:16:35', 0, 0),
(36, '20180505195015_U', '20180506111706_EBS', 'login登录模块', '1', 1, '1', 0, 3, 0, '第四个版本', '/static/codeSavePosition/20180505195015_U/20180506111706_EBS/login.zip', '2018-05-06 11:17:06', 0, 0),
(37, '20180506113447_q', '20180506113447_eFN', '阿斯达大法师', '3', 1, '1', 0, 5, 0, '第一个版本', '/static/codeSavePosition/20180506113447_q/20180506113447_eFN/login.zip', '2018-05-06 11:34:47', 1, 0),
(38, '20180506113447_q', '20180506113507_IWC', '阿斯达大法师', '3', 1, '1', 0, 8, 0, '第二个版本', '/static/codeSavePosition/20180506113447_q/20180506113507_IWC/login.zip', '2018-05-06 11:35:07', 0, 0),
(39, '20180507131912_2', '20180507131912_i6d', '这是为了测试程序库', '1', 1, '2', 0, 23, 0, '打扫收拾收拾收拾收拾收拾书', '/static/codeSavePosition/20180507131912_2/20180507131912_i6d/login.zip', '2018-05-07 13:19:12', 1, 0),
(40, '20180507140051_W', '20180507140051_ZMt', '标志位', '1', 1, '3', 0, 21, 0, '为了测试主程序标志位的第一个版本', '/static/codeSavePosition/20180507140051_W/20180507140051_ZMt/login.zip', '2018-05-07 14:00:51', 1, 0),
(41, '20180507140051_W', '20180507140207_8uK', '标志位', '1', 1, '3', 0, 10, 0, '为了测试程序标志位的第二个版本', '/static/codeSavePosition/20180507140051_W/20180507140207_8uK/login.zip', '2018-05-07 14:02:07', 0, 0),
(42, '20180509114226_S', '20180509114226_wZc', '测试工程访问', '3', 0, '1', 0, 52, 0, '为了测试此工程的访问权限', '/static/codeSavePosition/20180509114226_S/20180509114226_wZc/login.zip', '2018-05-09 11:42:26', 1, 0),
(43, '20180507140051_W', '20180510211205_YOh', '标志位', '1', 1, '3', 0, 11, 0, '第三次提交', '/static/codeSavePosition/20180507140051_W/20180510211205_YOh/login.zip', '2018-05-10 21:12:05', 0, 0),
(44, '20180502161746_7', '20180511184256_hXW', '四Q软件', '1', 1, '1', 0, 22, 0, '第二个版本', '/static/codeSavePosition/20180502161746_7/20180511184256_hXW/codeManageAndShare1.zip', '2018-05-11 18:42:56', 0, 1),
(45, '20180502161746_7', '20180511184354_EkJ', '四Q软件', '1', 1, '1', 0, 27, 0, '第三个版本', '/static/codeSavePosition/20180502161746_7/20180511184354_EkJ/codeManageAndShare1.zip', '2018-05-11 18:43:54', 0, 0),
(46, '20180502161746_7', '20180511184531_oKP', '四Q软件', '1', 1, '1', 0, 387, 0, '第四个版本', '/static/codeSavePosition/20180502161746_7/20180511184531_oKP/codeManageAndShare1.zip', '2018-05-11 18:45:31', 0, 0),
(47, '20180502161746_7', '20180511184725_oWO', '四Q软件', '1', 1, '1', 0, 14, 0, '第五个版本', '/static/codeSavePosition/20180502161746_7/20180511184725_oWO/codeManageAndShare1.zip', '2018-05-11 18:47:25', 0, 0),
(48, '20180515104139_x', '20180515104139_0a1', '版本控制', '1', 1, '9', 0, 6, 0, '为了验证版本控制：第一个版本', '/static/codeSavePosition/20180515104139_x/20180515104139_0a1/login.zip', '2018-05-15 10:41:39', 1, 1),
(49, '20180515104139_x', '20180515104332_JQq', '版本控制', '1', 1, '9', 0, 4, 0, '这是第二个版本，进行了删除、增加、修改的文件', '/static/codeSavePosition/20180515104139_x/20180515104332_JQq/login.zip', '2018-05-15 10:43:32', 0, 1),
(50, '20180515104139_x', '20180515133126_h93', '版本控制', '1', 1, '9', 0, 5, 0, '第三个版本', '/static/codeSavePosition/20180515104139_x/20180515133126_h93/login.zip', '2018-05-15 13:31:26', 0, 1);

-- --------------------------------------------------------

--
-- 表的结构 `app_codeManage_codetag`
--

CREATE TABLE IF NOT EXISTS `app_codeManage_codetag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codeTagName` varchar(20) NOT NULL,
  `codeTagClickTimes` int(11) NOT NULL,
  `codeTagLastClick` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=25 ;

--
-- 转存表中的数据 `app_codeManage_codetag`
--

INSERT INTO `app_codeManage_codetag` (`id`, `codeTagName`, `codeTagClickTimes`, `codeTagLastClick`) VALUES
(1, '有趣', 23, '2018-05-24 19:40:14'),
(2, '啦啦', 24, '2018-05-19 19:20:16'),
(3, '额额', 16, '2018-05-15 14:10:48'),
(4, '更改', 22, '2018-05-24 19:40:19'),
(5, '万维网', 21, '2018-05-24 19:40:17'),
(6, '吖吖', 3, '2018-05-11 16:16:31'),
(7, '达到', 4, '2018-05-12 23:19:51'),
(8, '单独', 7, '2018-05-19 17:06:30'),
(9, '搜索', 1, '2018-05-09 20:28:50'),
(10, '部分', 0, '2018-04-30 21:32:23'),
(11, '打算', 0, '2018-04-30 21:34:26'),
(12, '打发', 1, '2018-05-09 20:34:11'),
(13, '吖吖', 0, '2018-04-30 21:39:21'),
(14, '不让发', 0, '2018-04-30 21:42:17'),
(15, '阿斯达', 5, '2018-05-14 17:39:05'),
(16, '而非', 0, '2018-04-30 21:48:32'),
(17, '大桥', 10, '2018-05-10 21:02:51'),
(18, '速度', 0, '2018-05-01 19:25:22'),
(19, '大人', 0, '2018-05-01 19:26:47'),
(20, '发到', 35, '2018-05-19 19:20:11'),
(21, '撒大网', 0, '2018-05-01 19:32:01'),
(22, '娃娃店', 2, '2018-05-15 15:02:15'),
(23, '发送', 14, '2018-05-15 15:02:14'),
(24, '登录', 16, '2018-05-19 19:46:58');

-- --------------------------------------------------------

--
-- 表的结构 `app_codeManage_codetagrelation`
--

CREATE TABLE IF NOT EXISTS `app_codeManage_codetagrelation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codeTagRelationiCodeID` varchar(20) NOT NULL,
  `codeTagRelationTagID` varchar(20) NOT NULL,
  `codeTagRelationTime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=65 ;

--
-- 转存表中的数据 `app_codeManage_codetagrelation`
--

INSERT INTO `app_codeManage_codetagrelation` (`id`, `codeTagRelationiCodeID`, `codeTagRelationTagID`, `codeTagRelationTime`) VALUES
(36, '24', '23', '2018-05-01 22:49:17'),
(37, '24', '1', '2018-05-01 22:49:17'),
(38, '24', '7', '2018-05-01 22:49:17'),
(39, '24', '18', '2018-05-01 22:49:17'),
(40, '25', '8', '2018-05-02 16:16:01'),
(41, '25', '17', '2018-05-02 16:16:01'),
(42, '25', '20', '2018-05-02 16:16:01'),
(43, '26', '15', '2018-05-02 16:17:46'),
(44, '29', '3', '2018-05-02 16:30:38'),
(45, '29', '6', '2018-05-02 16:30:39'),
(46, '29', '8', '2018-05-02 16:30:39'),
(51, '33', '24', '2018-05-05 19:50:15'),
(52, '37', '1', '2018-05-06 11:34:47'),
(53, '37', '3', '2018-05-06 11:34:47'),
(54, '37', '5', '2018-05-06 11:34:47'),
(55, '39', '1', '2018-05-07 13:19:12'),
(56, '39', '4', '2018-05-07 13:19:12'),
(57, '39', '18', '2018-05-07 13:19:12'),
(58, '40', '8', '2018-05-07 14:00:51'),
(59, '40', '21', '2018-05-07 14:00:51'),
(60, '42', '8', '2018-05-09 11:42:26'),
(61, '42', '20', '2018-05-09 11:42:27'),
(62, '42', '23', '2018-05-09 11:42:27'),
(63, '48', '5', '2018-05-15 10:41:39'),
(64, '48', '23', '2018-05-15 10:41:39');

-- --------------------------------------------------------

--
-- 表的结构 `app_register_nomal_user`
--

CREATE TABLE IF NOT EXISTS `app_register_nomal_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nomal_username` varchar(30) NOT NULL,
  `nomal_usersex` varchar(5) NOT NULL,
  `nomal_usergradeclass` varchar(100) NOT NULL,
  `nomal_usernumber` varchar(20) NOT NULL,
  `nomal_useremail` varchar(254) NOT NULL,
  `nomal_useremailconfirm` varchar(10) NOT NULL,
  `nomal_userconfirmid` varchar(10) NOT NULL,
  `nomal_userImg` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

--
-- 转存表中的数据 `app_register_nomal_user`
--

INSERT INTO `app_register_nomal_user` (`id`, `nomal_username`, `nomal_usersex`, `nomal_usergradeclass`, `nomal_usernumber`, `nomal_useremail`, `nomal_useremailconfirm`, `nomal_userconfirmid`, `nomal_userImg`) VALUES
(1, '邵宁', 'man', '2014_2', '140104010034', '904809622@qq.com', 'ok', '10', '/static/selfPart/userImg/140104010034/5-160914192R2.gif'),
(2, '郑仲', 'man', '2014_2', '140104010035', '123456789@qq.com', 'ok', '11', '/static/selfPart/userImg/default.png'),
(3, '刘泽秋', 'woman', '2014_2', '140104010033', '123@qq.com', 'ok', '12', '/static/selfPart/userImg/140104010033/imgTest.jpg'),
(4, '谭明熙', 'woman', '2014_2', '140104010036', '9511900@qq.com', 'ok', '13', '/static/selfPart/userImg/default.png');

-- --------------------------------------------------------

--
-- 表的结构 `app_selfPart_selfpartfocusrelation`
--

CREATE TABLE IF NOT EXISTS `app_selfPart_selfpartfocusrelation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `selfPartFocusRelationOwnID` varchar(20) NOT NULL,
  `selfPartFocusRelationUserID` varchar(20) NOT NULL,
  `selfPartFocusRelationCodeID` varchar(20) NOT NULL,
  `selfPartFocusRelationTime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=15 ;

--
-- 转存表中的数据 `app_selfPart_selfpartfocusrelation`
--

INSERT INTO `app_selfPart_selfpartfocusrelation` (`id`, `selfPartFocusRelationOwnID`, `selfPartFocusRelationUserID`, `selfPartFocusRelationCodeID`, `selfPartFocusRelationTime`) VALUES
(2, '1', '2', '0', '2018-04-30 13:42:09'),
(13, '1', '3', '0', '2018-05-11 16:36:07');

-- --------------------------------------------------------

--
-- 表的结构 `app_selfPart_selfpartmessage`
--

CREATE TABLE IF NOT EXISTS `app_selfPart_selfpartmessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `selfPartMessageCreateTime` datetime NOT NULL,
  `selfPartMessageSendUserID` varchar(20) NOT NULL,
  `selfPartMessageReceUserID` varchar(20) NOT NULL,
  `selfPartMessageIsNew` tinyint(1) NOT NULL,
  `selfPartMessageContent` longtext NOT NULL,
  `selfPartMessageIsDeleteByRece` tinyint(1) NOT NULL,
  `selfPartMessageIsDeleteBySend` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=62 ;

--
-- 转存表中的数据 `app_selfPart_selfpartmessage`
--

INSERT INTO `app_selfPart_selfpartmessage` (`id`, `selfPartMessageCreateTime`, `selfPartMessageSendUserID`, `selfPartMessageReceUserID`, `selfPartMessageIsNew`, `selfPartMessageContent`, `selfPartMessageIsDeleteByRece`, `selfPartMessageIsDeleteBySend`) VALUES
(1, '2018-04-24 13:41:38', '1', '3', 0, '你好，我是邵宁', 1, 1),
(2, '2018-04-24 13:41:38', '3', '1', 0, '你好，我是刘泽秋', 1, 1),
(3, '2018-04-24 13:42:18', '1', '2', 0, '你好，我是邵宁', 0, 0),
(4, '2018-04-24 13:42:18', '2', '1', 0, '你好，我是郑仲', 0, 0),
(5, '2018-04-25 06:07:56', '4', '1', 0, '的发电示范', 0, 0),
(6, '2018-04-25 06:09:13', '4', '1', 0, '啦啦啦', 0, 0),
(7, '2018-04-25 06:10:29', '1', '4', 0, 'asd', 0, 0),
(8, '2018-04-25 06:11:39', '1', '3', 0, '嗯，我是邵宁', 1, 1),
(9, '2018-04-25 06:12:16', '3', '1', 0, '我是刘泽秋', 1, 1),
(10, '2018-04-25 06:17:42', '1', '4', 0, 'af', 0, 0),
(11, '2018-04-25 06:17:53', '3', '1', 0, '哈哈', 1, 1),
(12, '2018-04-25 06:18:09', '3', '1', 0, '大时代', 1, 1),
(13, '2018-04-25 06:18:10', '3', '1', 0, ' ad', 1, 1),
(14, '2018-04-25 06:18:12', '3', '1', 0, 'dasd啊', 1, 1),
(15, '2018-04-25 06:18:37', '1', '3', 0, '阿凡达', 1, 1),
(16, '2018-04-25 06:18:39', '1', '3', 0, '发生大幅', 1, 1),
(17, '2018-04-25 06:25:26', '3', '1', 0, '发生大幅', 1, 1),
(18, '2018-04-25 06:25:29', '3', '1', 0, '大叔大婶', 1, 1),
(19, '2018-04-25 14:47:35', '3', '1', 0, '撒旦大S的', 1, 1),
(20, '2018-04-25 14:48:34', '3', '1', 0, '哪个服', 1, 1),
(21, '2018-04-25 14:48:54', '3', '1', 0, '大时代', 1, 1),
(22, '2018-04-25 15:40:26', '3', '1', 0, 'ASDASD', 1, 1),
(23, '2018-04-25 15:40:33', '1', '3', 0, 'SDAASDA', 1, 1),
(24, '2018-04-25 15:40:50', '1', '3', 0, 'GARGS', 1, 1),
(25, '2018-04-25 20:35:30', '1', '3', 0, '而对方SD酚A', 1, 1),
(26, '2018-04-25 21:49:55', '1', '3', 0, 'fadsfasfasd', 1, 1),
(27, '2018-04-25 21:50:03', '3', '1', 0, 'sdas发生的', 1, 1),
(28, '2018-04-28 10:54:03', '1', '3', 0, 'aaaa', 1, 1),
(29, '2018-04-28 10:54:36', '3', '1', 0, 'aaaa', 1, 1),
(30, '2018-04-28 10:54:44', '3', '1', 0, 'adsd', 1, 1),
(31, '2018-04-28 10:55:01', '1', '3', 0, '发生大幅', 1, 1),
(32, '2018-04-28 11:01:13', '3', '1', 0, 'dfas', 1, 1),
(33, '2018-04-28 11:01:24', '3', '1', 0, 'cdssadf', 1, 1),
(34, '2018-04-28 11:02:48', '3', '1', 0, 'efasfsdf', 1, 1),
(35, '2018-04-28 11:03:23', '3', '1', 0, 'fsdfse', 1, 1),
(36, '2018-04-28 11:03:58', '3', '1', 0, 'dasdas', 1, 1),
(37, '2018-04-28 11:04:06', '3', '1', 0, 'aaaaaa', 1, 1),
(38, '2018-04-28 11:04:13', '3', '1', 0, 'sas', 1, 1),
(39, '2018-04-28 11:04:49', '3', '1', 0, 'dasd', 1, 1),
(40, '2018-04-28 11:04:55', '3', '1', 0, 'sdasdasd', 1, 1),
(41, '2018-04-28 11:05:00', '1', '3', 0, '大时代', 1, 1),
(42, '2018-04-28 14:14:18', '3', '1', 0, '1565', 1, 1),
(43, '2018-04-28 14:14:23', '1', '3', 0, '1561', 1, 1),
(44, '2018-04-28 14:14:27', '1', '3', 0, '156165165165', 1, 1),
(45, '2018-04-28 14:14:30', '1', '3', 0, '56165', 1, 1),
(46, '2018-04-29 10:37:01', '3', '1', 0, '5555', 1, 1),
(47, '2018-04-29 10:37:19', '3', '1', 0, '似懂非懂', 1, 1),
(48, '2018-04-29 10:37:25', '3', '1', 0, '而说法', 1, 1),
(49, '2018-04-30 15:40:17', '3', '1', 0, '快乐；即可', 1, 1),
(53, '2018-05-11 14:53:50', '3', '2', 0, '1156156', 0, 0),
(54, '2018-05-15 13:45:28', '1', '2', 0, '151', 0, 0),
(55, '2018-05-15 13:50:07', '1', '2', 0, '打算', 0, 0),
(56, '2018-05-15 20:33:51', '1', '2', 0, '4141964', 0, 0),
(57, '2018-05-16 20:19:23', '3', '1', 0, '111', 1, 0),
(58, '2018-05-16 20:28:10', '3', '1', 0, '5555555555', 0, 0),
(59, '2018-05-16 20:31:19', '3', '1', 0, '你发', 0, 0),
(60, '2018-05-24 19:42:27', '3', '1', 0, '111', 0, 0),
(61, '2018-05-24 19:42:37', '1', '3', 0, '4523', 0, 0);

-- --------------------------------------------------------

--
-- 表的结构 `app_selfPart_selfpartmyfriends`
--

CREATE TABLE IF NOT EXISTS `app_selfPart_selfpartmyfriends` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `selfPartFriendDoneTime` datetime NOT NULL,
  `selfPartOwnID` varchar(20) NOT NULL,
  `selfPartFriendID` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=10 ;

--
-- 转存表中的数据 `app_selfPart_selfpartmyfriends`
--

INSERT INTO `app_selfPart_selfpartmyfriends` (`id`, `selfPartFriendDoneTime`, `selfPartOwnID`, `selfPartFriendID`) VALUES
(1, '2018-04-24 23:00:00', '1', '2'),
(2, '2018-04-24 23:00:00', '2', '1'),
(4, '2018-04-24 11:05:28', '3', '1'),
(5, '2018-04-25 12:39:38', '1', '4'),
(6, '2018-04-25 12:39:38', '4', '1'),
(7, '2018-05-11 14:53:27', '3', '2'),
(9, '2018-05-12 11:02:04', '1', '3');

-- --------------------------------------------------------

--
-- 表的结构 `app_selfPart_selfpartuserdynamic`
--

CREATE TABLE IF NOT EXISTS `app_selfPart_selfpartuserdynamic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `selfPartUserDynamicUserID` varchar(10) NOT NULL,
  `selfPartUserDynamicType` varchar(30) NOT NULL,
  `selfPartUserDynamicPic` varchar(20) NOT NULL,
  `selfPartUserDynamicExplain` longtext NOT NULL,
  `selfPartUserDynamicCodeID` varchar(10) NOT NULL,
  `selfPartUserDynamicTime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=46 ;

--
-- 转存表中的数据 `app_selfPart_selfpartuserdynamic`
--

INSERT INTO `app_selfPart_selfpartuserdynamic` (`id`, `selfPartUserDynamicUserID`, `selfPartUserDynamicType`, `selfPartUserDynamicPic`, `selfPartUserDynamicExplain`, `selfPartUserDynamicCodeID`, `selfPartUserDynamicTime`) VALUES
(12, '1', 'data_addDate', 'xe690', '', '24', '2018-05-01 22:49:17'),
(13, '1', 'data_addDate', 'xe690', '', '25', '2018-05-02 16:16:01'),
(14, '1', 'data_addDate', 'xe690', '', '26', '2018-05-02 16:17:47'),
(16, '1', 'data_addDate', 'xe690', '', '28', '2018-05-02 16:27:55'),
(17, '1', 'data_addDate', 'xe690', '', '29', '2018-05-02 16:30:39'),
(20, '1', 'data_update', 'xe665', '', '31', '2018-05-05 19:18:54'),
(21, '1', 'data_update', 'xe665', '', '32', '2018-05-05 19:43:35'),
(22, '1', 'data_addDate', 'xe690', '', '33', '2018-05-05 19:50:15'),
(23, '1', 'data_update', 'xe665', '', '34', '2018-05-05 19:51:47'),
(24, '1', 'data_update', 'xe665', '', '35', '2018-05-06 11:16:35'),
(25, '1', 'data_update', 'xe665', '', '36', '2018-05-06 11:17:06'),
(26, '3', 'data_addDate', 'xe690', '', '37', '2018-05-06 11:34:47'),
(27, '3', 'data_update', 'xe665', '', '38', '2018-05-06 11:35:07'),
(28, '1', 'data_addDate', 'xe690', '', '39', '2018-05-07 13:19:12'),
(29, '1', 'data_addDate', 'xe690', '', '40', '2018-05-07 14:00:51'),
(30, '1', 'data_update', 'xe665', '', '41', '2018-05-07 14:02:07'),
(31, '3', 'data_addDate', 'xe690', '', '42', '2018-05-09 11:42:27'),
(32, '1', 'data_update', 'xe665', '', '43', '2018-05-10 21:12:05'),
(33, '1', 'data_update', 'xe665', '', '44', '2018-05-11 18:42:56'),
(34, '1', 'data_update', 'xe665', '', '45', '2018-05-11 18:43:54'),
(35, '1', 'data_update', 'xe665', '', '46', '2018-05-11 18:45:32'),
(36, '1', 'data_update', 'xe665', '', '47', '2018-05-11 18:47:25'),
(37, '1', 'data_addDate', 'xe690', '', '48', '2018-05-15 10:41:39'),
(38, '1', 'data_update', 'xe665', '', '49', '2018-05-15 10:43:32'),
(39, '1', 'data_update', 'xe665', '', '50', '2018-05-15 13:31:26'),
(40, '1', 'data_delDate', 'xe663', '', '44', '2018-05-15 14:48:02'),
(42, '1', 'data_delDate', 'xe663', '', '50', '2018-05-15 14:56:58'),
(43, '1', 'data_delDate', 'xe663', '', '48', '2018-05-15 14:57:38'),
(44, '1', 'data_delDate', 'xe663', '', '49', '2018-05-15 14:58:28'),
(45, '1', 'data_delDate', 'xe663', '', '32', '2018-05-16 13:45:40');

-- --------------------------------------------------------

--
-- 表的结构 `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- 转存表中的数据 `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'addAllPremissions');

-- --------------------------------------------------------

--
-- 表的结构 `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=46 ;

--
-- 转存表中的数据 `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 1, 6),
(7, 1, 7),
(8, 1, 8),
(9, 1, 9),
(10, 1, 10),
(11, 1, 11),
(12, 1, 12),
(13, 1, 13),
(14, 1, 14),
(15, 1, 15),
(16, 1, 16),
(17, 1, 17),
(18, 1, 18),
(19, 1, 19),
(20, 1, 20),
(21, 1, 21),
(22, 1, 22),
(23, 1, 23),
(24, 1, 24),
(25, 1, 25),
(26, 1, 26),
(27, 1, 27),
(28, 1, 28),
(29, 1, 29),
(30, 1, 30),
(31, 1, 31),
(32, 1, 32),
(33, 1, 33),
(34, 1, 34),
(35, 1, 35),
(36, 1, 36),
(37, 1, 37),
(38, 1, 38),
(39, 1, 39),
(40, 1, 40),
(41, 1, 41),
(42, 1, 42),
(43, 1, 43),
(44, 1, 44),
(45, 1, 45);

-- --------------------------------------------------------

--
-- 表的结构 `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=49 ;

--
-- 转存表中的数据 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add permission', 3, 'add_permission'),
(8, 'Can change permission', 3, 'change_permission'),
(9, 'Can delete permission', 3, 'delete_permission'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add nomal_user', 7, 'add_nomal_user'),
(20, 'Can change nomal_user', 7, 'change_nomal_user'),
(21, 'Can delete nomal_user', 7, 'delete_nomal_user'),
(22, 'Can add self part message', 8, 'add_selfpartmessage'),
(23, 'Can change self part message', 8, 'change_selfpartmessage'),
(24, 'Can delete self part message', 8, 'delete_selfpartmessage'),
(25, 'Can add self part my friends', 9, 'add_selfpartmyfriends'),
(26, 'Can change self part my friends', 9, 'change_selfpartmyfriends'),
(27, 'Can delete self part my friends', 9, 'delete_selfpartmyfriends'),
(28, 'Can add self part focus relation', 10, 'add_selfpartfocusrelation'),
(29, 'Can change self part focus relation', 10, 'change_selfpartfocusrelation'),
(30, 'Can delete self part focus relation', 10, 'delete_selfpartfocusrelation'),
(31, 'Can add code manage', 11, 'add_codemanage'),
(32, 'Can change code manage', 11, 'change_codemanage'),
(33, 'Can delete code manage', 11, 'delete_codemanage'),
(34, 'Can add code tag', 12, 'add_codetag'),
(35, 'Can change code tag', 12, 'change_codetag'),
(36, 'Can delete code tag', 12, 'delete_codetag'),
(37, 'Can add code tag relation', 13, 'add_codetagrelation'),
(38, 'Can change code tag relation', 13, 'change_codetagrelation'),
(39, 'Can delete code tag relation', 13, 'delete_codetagrelation'),
(40, 'Can add self part user dynamic', 14, 'add_selfpartuserdynamic'),
(41, 'Can change self part user dynamic', 14, 'change_selfpartuserdynamic'),
(42, 'Can delete self part user dynamic', 14, 'delete_selfpartuserdynamic'),
(43, 'Can add code language', 15, 'add_codelanguage'),
(44, 'Can change code language', 15, 'change_codelanguage'),
(45, 'Can delete code language', 15, 'delete_codelanguage'),
(46, 'Can add code discuss', 16, 'add_codediscuss'),
(47, 'Can change code discuss', 16, 'change_codediscuss'),
(48, 'Can delete code discuss', 16, 'delete_codediscuss');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=15 ;

--
-- 转存表中的数据 `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(10, 'pbkdf2_sha256$36000$LElIHmjUZtS5$2GTuI4OsaTEtgi1eH2JGQx/u82qgHOggzWNHX/cgFvk=', '2018-05-25 10:17:12', 0, '140104010034', '邵宁', '', '904809622@qq.com', 0, 1, '2018-04-24 01:46:42'),
(11, 'pbkdf2_sha256$36000$AhOHD2WelUZs$QzciMvPwvlCX+xzW+lpoJM/qFdST9xchh3Gj8NpDZoQ=', '2018-05-11 14:54:05', 0, '140104010035', '郑仲', '', '123456789@qq.com', 0, 1, '2018-04-24 02:16:16'),
(12, 'pbkdf2_sha256$36000$1NdKyGCv6TD4$uXbLfIyny1bo4nrEd6uI/jQVndqFnjWEU54Ms6fumLE=', '2018-05-24 19:42:20', 0, '140104010033', '刘泽秋', '', '123@qq.com', 0, 1, '2018-04-24 03:03:37'),
(13, 'pbkdf2_sha256$36000$AYVHTOm1Upuv$eciQ4i9oLu/pW2WWPBd2Jbo29dQuPWi5rLkBsNfFlKw=', '2018-04-25 06:10:53', 0, '140104010036', '谭明熙', '', '9511900@qq.com', 0, 1, '2018-04-24 15:09:44'),
(14, 'pbkdf2_sha256$36000$Xt05rIfBy5kE$6wyGIj+Go7gBUwbUtuqvDyxy8d63hMB7UyAPNUsqvKY=', '2018-05-18 19:13:28', 1, 'shaoning', '', '', '904809622@qq.com', 1, 1, '2018-05-18 19:13:10');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- 转存表中的数据 `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2018-05-18 19:15:46', '1', 'addAllPremissions', 1, '[{"added": {}}]', 2, 14),
(2, '2018-05-18 19:15:51', '1', 'addAllPremissions', 2, '[]', 2, 14);

-- --------------------------------------------------------

--
-- 表的结构 `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=17 ;

--
-- 转存表中的数据 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(16, 'app_codeManage', 'codediscuss'),
(15, 'app_codeManage', 'codelanguage'),
(11, 'app_codeManage', 'codemanage'),
(12, 'app_codeManage', 'codetag'),
(13, 'app_codeManage', 'codetagrelation'),
(7, 'app_register', 'nomal_user'),
(10, 'app_selfPart', 'selfpartfocusrelation'),
(8, 'app_selfPart', 'selfpartmessage'),
(9, 'app_selfPart', 'selfpartmyfriends'),
(14, 'app_selfPart', 'selfpartuserdynamic'),
(2, 'auth', 'group'),
(3, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- 表的结构 `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=41 ;

--
-- 转存表中的数据 `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-04-22 03:47:07'),
(2, 'auth', '0001_initial', '2018-04-22 03:47:08'),
(3, 'admin', '0001_initial', '2018-04-22 03:47:08'),
(4, 'admin', '0002_logentry_remove_auto_add', '2018-04-22 03:47:08'),
(6, 'contenttypes', '0002_remove_content_type_name', '2018-04-22 03:47:08'),
(7, 'auth', '0002_alter_permission_name_max_length', '2018-04-22 03:47:09'),
(8, 'auth', '0003_alter_user_email_max_length', '2018-04-22 03:47:09'),
(9, 'auth', '0004_alter_user_username_opts', '2018-04-22 03:47:09'),
(10, 'auth', '0005_alter_user_last_login_null', '2018-04-22 03:47:09'),
(11, 'auth', '0006_require_contenttypes_0002', '2018-04-22 03:47:09'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2018-04-22 03:47:09'),
(13, 'auth', '0008_alter_user_username_max_length', '2018-04-22 03:47:09'),
(14, 'sessions', '0001_initial', '2018-04-22 03:47:09'),
(24, 'app_selfPart', '0001_initial', '2018-04-23 15:33:23'),
(25, 'app_register', '0001_initial', '2018-04-24 01:44:24'),
(26, 'app_register', '0002_nomal_user_nomal_userimg', '2018-04-24 02:04:34'),
(27, 'app_selfPart', '0002_selfpartmyfriends', '2018-04-24 02:11:06'),
(29, 'app_selfPart', '0002_selfpartfocusrelation', '2018-04-26 09:29:49'),
(30, 'app_selfPart', '0003_selfpartuserdynamic', '2018-04-26 10:58:14'),
(31, 'app_codeManage', '0001_initial', '2018-04-26 11:01:58'),
(33, 'app_codeManage', '0002_codelanguage', '2018-04-28 17:35:39'),
(34, 'app_codeManage', '0003_codemanage_codemanagemainflag', '2018-05-07 13:57:23'),
(35, 'app_codeManage', '0004_codemanage_codemanageisdelete', '2018-05-15 14:38:48'),
(36, 'app_selfPart', '0004_selfpartmessage_selfpartmessageisdelete', '2018-05-15 20:12:39'),
(37, 'app_selfPart', '0005_auto_20180516_2012', '2018-05-16 20:12:59'),
(38, 'app_codeManage', '0005_codediscuss', '2018-05-19 13:06:35'),
(39, 'app_codeManage', '0006_codediscuss_codediscusscontent', '2018-05-19 13:32:36'),
(40, 'app_codeManage', '0007_auto_20180519_1850', '2018-05-19 18:50:13');

-- --------------------------------------------------------

--
-- 表的结构 `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ckgl875krwxxfl6fg4kqjdrpn0opbq2l', 'NzVjMzQ0Mzc2NjRhYzA5ZWQwY2Q5YzNmZjRiZjk3YzZjZDhjYzBlZTp7Il9hdXRoX3VzZXJfaGFzaCI6ImU5MjU4YTdkYWUxZTMxY2U1YzVjYTYyNzllZDY2YmJmMjhmOTExNzYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMCJ9', '2018-06-08 10:17:12');

--
-- 限制导出的表
--

--
-- 限制表 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- 限制表 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- 限制表 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
