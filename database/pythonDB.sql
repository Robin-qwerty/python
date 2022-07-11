-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 11, 2022 at 07:10 PM
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
(7, 1, 35, 'https://droneshop.nl/radiomaster-tx16s'),
(8, 2, 35, ''),
(9, 1, 37, 'https://droneshop.nl/dji-mini-2');

-- --------------------------------------------------------

--
-- Table structure for table `product_track`
--

CREATE TABLE `product_track` (
  `id` int(11) NOT NULL,
  `product_info` int(11) NOT NULL,
  `price` decimal(9,0) NOT NULL,
  `stock` tinyint(1) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `product_track`
--

INSERT INTO `product_track` (`id`, `product_info`, `price`, `stock`, `date`) VALUES
(1, 7, '198', 0, '2022-07-11'),
(2, 8, '200', 0, '2022-07-11'),
(3, 9, '449', 1, '2022-07-11');

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
(1, 'droneshop'),
(2, 'getfpv');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `product_info`
--
ALTER TABLE `product_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `product_track`
--
ALTER TABLE `product_track`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `website`
--
ALTER TABLE `website`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `product_info`
--
ALTER TABLE `product_info`
  ADD CONSTRAINT `product_info_ibfk_1` FOREIGN KEY (`product`) REFERENCES `product` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `product_track`
--
ALTER TABLE `product_track`
  ADD CONSTRAINT `product_track_ibfk_1` FOREIGN KEY (`product_info`) REFERENCES `product_info` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `website`
--
ALTER TABLE `website`
  ADD CONSTRAINT `website_ibfk_1` FOREIGN KEY (`id`) REFERENCES `product_info` (`website`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
