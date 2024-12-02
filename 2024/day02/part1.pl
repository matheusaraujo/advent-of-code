#!/usr/bin/perl
use strict;
use warnings;

sub part1 {
    my @input        = @_;
    my $safe_reports = 0;

    foreach (@input) {
        my @report = split " ", $_;
        if ( is_safe_report(@report) ) {
            $safe_reports++;
        }
    }

    return $safe_reports;
}

1;
