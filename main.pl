#!/usr/bin/perl
use strict;
use warnings;

use Time::HiRes qw(time);
use feature 'say';

my $year = $ARGV[0];
my $day  = $ARGV[1];
my $file = $ARGV[2];

use Carp;

$year or croak 'year is required';
$day  or croak 'day is required';

do "./$year/day$day/part1.pl" or croak 'could not load part1.pl';
do "./$year/day$day/part2.pl" or croak 'could not load part2.pl';

my $input_file;
if (defined $file) {
    $input_file = "$year/day$day/$file.in";
} else {
    $input_file = "$year/day$day/input.txt";
}

my $output_file;
if (defined $file) {
    $output_file = "$year/day$day/$file.out";
}

open my $fh_input, '<', $input_file
  or croak 'could not open input file';
my @input = <$fh_input>;
close $fh_input or croak 'could not close input file';

my $output;
if (defined $output_file) {
    open my $fh_output, '<', $output_file
      or croak 'could not open output file';
    $output = <$fh_output>;
    close $fh_output or croak 'could not close output file';
}

if ( defined $file ) {
    print "Advent of Code - $year, Day $day - Test: $file\n";
} else {
  print "Advent of Code - $year, Day $day\n";
}

if (!defined $file || $file=~ /^[1]/smx) {
  my $start_time1   = time;
  my $result1       = part1(@input);
  my $end_time1     = time;
  my $elapsed_time1 = $end_time1 - $start_time1;

  print "part1.pl: $result1 - " . sprintf "%.4fms\n", $elapsed_time1 * 1000;

  if ( defined $output && $result1 ne $output ) {
      print "Expected: $output\n";
      croak 'part1.pl: result does not match expected output';
  }
}

if (!defined $file || $file=~ /^[2]/smx) {
  my $start_time2   = time;
  my $result2       = part2(@input);
  my $end_time2     = time;
  my $elapsed_time2 = $end_time2 - $start_time2;

  print "part2.pl: $result2 - " . sprintf "%.4fms\n", $elapsed_time2 * 1000;

  if ( defined $output && $result2 ne $output ) {
      print "Expected: $output\n";
      croak 'part2.pl: result does not match expected output';
  }
}
