-- phpMyAdmin SQL Dump
-- version 5.3.0-dev+20220408.20e55eb1ac
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 14, 2022 at 10:03 AM
-- Server version: 10.6.8-MariaDB
-- PHP Version: 8.1.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythonDB`
--

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `name` varchar(88) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `name`) VALUES
(35, 'RadioMaster TX16S'),
(37, 'DJI Mini 2');

-- --------------------------------------------------------

--
-- Table structure for table `product_info`
--

CREATE TABLE `product_info` (
  `id` int(11) NOT NULL,
  `website` int(11) NOT NULL,
  `product` int(11) NOT NULL,
  `url` varchar(111) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `product_info`
--

INSERT INTO `product_info` (`id`, `website`, `product`, `url`) VALUES
(20, 1, 35, 'https://droneshop.nl/radiomaster-tx16s'),
(21, 5, 35, 'https://www.unmannedtechshop.co.uk/product/radiomaster-tx16s-mkii/'),
(22, 2, 35, 'https://www.getfpv.com/radiomaster-tx16s-multi-protocol-rf-2-4ghz-16ch-radio-transmitter-hall-gimbal-black.html'),
(26, 6, 35, 'https://www.hobbyrc.co.uk/radiomaster-tx16s-mkii-hall-gimbal-transmitter-4in1'),
(27, 3, 35, 'https://airjacker.com/products/radiomaster-t16s-mkii-4-in-1?_pos=4&_sid=5621d72d8&_ss=r'),
(28, 4, 35, 'https://yourfpv.co.uk/product/radiomaster-tx16s-hall-gimbal-transmitter/');

-- --------------------------------------------------------

--
-- Table structure for table `product_track`
--

CREATE TABLE `product_track` (
  `id` int(11) NOT NULL,
  `product_info` int(11) NOT NULL,
  `price` decimal(9,2) NOT NULL,
  `price_usd` decimal(9,2) DEFAULT NULL,
  `price_pounds` decimal(9,2) DEFAULT NULL,
  `stock` tinyint(1) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `product_track`
--

INSERT INTO `product_track` (`id`, `product_info`, `price`, `price_usd`, `price_pounds`, `stock`, `date`) VALUES
(7, 20, '198.00', NULL, NULL, 0, '2022-07-13'),
(8, 21, '212.39', NULL, '179.99', 0, '2022-07-13'),
(9, 22, '198.59', '199.99', NULL, 0, '2022-07-13'),
(12, 26, '212.39', NULL, '179.99', 0, '2022-07-13'),
(13, 27, '212.28', NULL, '179.90', 1, '2022-07-13'),
(14, 28, '188.79', NULL, '159.99', 0, '2022-07-13');

-- --------------------------------------------------------

--
-- Table structure for table `website`
--

CREATE TABLE `website` (
  `id` int(11) NOT NULL,
  `website` varchar(33) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `website`
--

INSERT INTO `website` (`id`, `website`) VALUES
(3, 'airjacker'),
(1, 'droneshop'),
(2, 'getfpv'),
(6, 'hobbyrc'),
(5, 'unmannedtechshop'),
(4, 'yourfpv');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `product_info`
--
ALTER TABLE `product_info`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product` (`product`),
  ADD KEY `shop` (`website`),
  ADD KEY `id` (`id`),
  ADD KEY `website` (`website`);

--
-- Indexes for table `product_track`
--
ALTER TABLE `product_track`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product_info` (`product_info`);

--
-- Indexes for table `website`
--
ALTER TABLE `website`
  ADD PRIMARY KEY (`id`),
  ADD KEY `website` (`website`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `product_info`
--
ALTER TABLE `product_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `product_track`
--
ALTER TABLE `product_track`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `website`
--
ALTER TABLE `website`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `product_info`
--
ALTER TABLE `product_info`
  ADD CONSTRAINT `product_info_ibfk_1` FOREIGN KEY (`product`) REFERENCES `product` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `product_info_ibfk_2` FOREIGN KEY (`website`) REFERENCES `website` (`id`);

--
-- Constraints for table `product_track`
--
ALTER TABLE `product_track`
  ADD CONSTRAINT `product_track_ibfk_1` FOREIGN KEY (`product_info`) REFERENCES `product_info` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
