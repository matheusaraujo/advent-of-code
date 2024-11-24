#!/usr/bin/perl
use strict;
use warnings;

use Time::HiRes qw(time);
use feature 'say';
use Carp;

sub main {
    my ( $year, $day, $file ) = @ARGV;
    validate_inputs( $year, $day );

    my ( $input_file, $output_file ) = get_file_paths( $year, $day, $file );
    my @input = read_file($input_file);
    my $expected_output =
      $output_file ? read_file( $output_file, scalar => 1 ) : undef;

    print_header( $year, $day, $file );

    if ( !defined $file || $file =~ /^[1]/smx ) {
        execute_part( 'part1', \&part1, \@input, $expected_output );
    }

    if ( !defined $file || $file =~ /^[2]/smx ) {
        execute_part( 'part2', \&part2, \@input, $expected_output );
    }

    return;
}

sub validate_inputs {
    my ( $year, $day ) = @_;
    if ( !$year ) {
        croak 'year is required';
    }
    if ( !$day ) {
        croak 'day is required';
    }

    do "./$year/day$day/part1.pl" or croak 'could not load part1.pl';
    do "./$year/day$day/part2.pl" or croak 'could not load part2.pl';

    return;
}

sub get_file_paths {
    my ( $year, $day, $file ) = @_;
    my $input_file =
      defined $file ? "$year/day$day/$file.in" : "$year/day$day/input.txt";
    my $output_file = defined $file ? "$year/day$day/$file.out" : undef;
    return ( $input_file, $output_file );
}

sub read_file {
    my ( $file_path, %opts ) = @_;
    open my $fh, '<', $file_path or croak "could not open file: $file_path";
    my @lines = <$fh>;
    close $fh or croak "could not close file: $file_path";
    return $opts{scalar} ? $lines[0] : @lines;
}

sub print_header {
    my ( $year, $day, $file ) = @_;
    if ( defined $file ) {
        say "Advent of Code - $year, Day $day - Test: $file";
    }
    else {
        say "Advent of Code - $year, Day $day";
    }
    return;
}

sub execute_part {
    my ( $part_name, $part_function, $input_ref, $expected_output ) = @_;
    my $start_time   = time;
    my $result       = $part_function->( @{$input_ref} );
    my $end_time     = time;
    my $elapsed_time = $end_time - $start_time;

    say $part_name . ": $result - " . sprintf '%.4fms', $elapsed_time * 1000;

    if ( defined $expected_output && $result ne $expected_output ) {
        say "Expected: $expected_output";
        croak "$part_name: result does not match expected output";
    }
}

main();
