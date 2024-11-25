#!/usr/bin/perl
use strict;
use warnings;

use Time::HiRes qw(time);
use feature 'say';
use Carp;

sub main {
    my ( $year, $day, $part_name, $input_file, $output_file ) = @ARGV;

    my @input = read_file($input_file);
    my $expected_output = $output_file ? read_file($output_file, scalar => 1) : undef;

    my $script_path = get_script_path( $year, $day, $part_name );
    load_script($script_path);

    my $part_function = \&{$part_name};
    execute_part( $part_name, $input_file, $part_function, \@input, $expected_output );
}

sub get_script_path {
    my ( $year, $day, $part_name ) = @_;
    return "./$year/day$day/$part_name.pl";
}

sub load_script {
    my ($script_path) = @_;
    do $script_path or croak "Could not load script '$script_path': $!";
}

sub read_file {
    my ( $file_path, %opts ) = @_;
    open my $fh, '<', $file_path or croak "Could not open file '$file_path': $!";
    my @lines = <$fh>;
    close $fh or croak "Could not close file '$file_path': $!";
    return $opts{scalar} ? $lines[0] : @lines;
}

sub execute_part {
    my ( $part_name, $input_file, $part_function, $input_ref, $expected_output ) = @_;

    my $input_file_label = get_input_file_label($input_file);

    my $start_time = time;
    my $result     = $part_function->(@$input_ref);
    my $end_time   = time;

    my $elapsed_time = sprintf '%.4fms', ($end_time - $start_time) * 1000;
    my ($result_check, $result_symbol) = get_result_symbol( $result, $expected_output );

    say format_result_message( $part_name, $input_file_label, $result, $elapsed_time, $result_symbol );

    if (!$result_check) {
        exit 1;
    }
}

sub get_input_file_label {
    my ($input_file) = @_;
    my $file_name = (split /\//, $input_file)[-1];
    return $file_name eq 'input.txt' ? '' : '(' . (split /\./, $file_name)[-2] . ')';
}

sub get_result_symbol {
    my ( $result, $expected_output ) = @_;
    return (1, '') unless defined $expected_output;
    my $is_equal = $result eq $expected_output;
    my $symbol = $is_equal ? "\033[32m✔\033[0m" : "\033[91m✘ $expected_output\033[0m";
    return ($is_equal, $symbol);
}

sub format_result_message {
    my ( $part_name, $input_file_label, $result, $elapsed_time, $result_symbol ) = @_;
    return sprintf(
        "\033[35m%s%s: \033[0m\033[32m%s\033[3;90m (executed in %s)%s\033[0m",
        $part_name, $input_file_label, $result, $elapsed_time, $result_symbol
    );
}

main();
