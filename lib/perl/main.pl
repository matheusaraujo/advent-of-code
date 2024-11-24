#!/usr/bin/perl
use strict;
use warnings;

use Time::HiRes qw(time);
use feature 'say';
use Carp;

sub main {
    my ( $year, $day, $part, $input_file, $output_file ) = @ARGV;

    my @input = read_file($input_file);
    my $expected_output =
      $output_file ? read_file( $output_file, scalar => 1 ) : undef;

    if ($part eq "part1") {
        do "./$year/day$day/part1.pl" or croak 'could not load part1.pl';
    }
    elsif ($part eq "part2") {
        do "./$year/day$day/part2.pl" or croak 'could not load part2.pl';
    }
    
    execute_part( $part, $input_file, \&$part, \@input, $expected_output );

    return;
}

sub read_file {
    my ( $file_path, %opts ) = @_;
    open my $fh, '<', $file_path or croak "could not open file: $file_path";
    my @lines = <$fh>;
    close $fh or croak "could not close file: $file_path";
    return $opts{scalar} ? $lines[0] : @lines;
}

sub execute_part {
    my ( $part_name, $input_file, $part_function, $input_ref, $expected_output ) = @_;
    my $input_file_name = (split /\//, $input_file)[-1];
    if ($input_file_name eq "input.txt") {
        $input_file_name = "";
    } else {
        $input_file_name = "(" . (split /\./, $input_file_name)[-2] . ")";
    }
    
    my $start_time   = time;
    my $result       = $part_function->( @{$input_ref} );
    my $end_time     = time;
    my $elapsed_time = $end_time - $start_time;

    my $result_symbol = "";

    if ( defined $expected_output) {
        if( $result eq $expected_output ) {
            $result_symbol = "\033[32m ✔ \033[0m";
        }
        else {
            $result_symbol = "\033[91m ✘ \033[0m";
        }
    }

    say "\033[35m".$part_name . "$input_file_name: " . "\033[0m" . 
        "\033[32m" . "$result" . "\033[3;90m (executed in " . (sprintf '%.4fms)', $elapsed_time * 1000) .
        $result_symbol . "\033[0m";

    
}

main();
