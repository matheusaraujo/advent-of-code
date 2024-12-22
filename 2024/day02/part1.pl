use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my $safe_reports = 0;

    foreach my $line (@puzzle_input) {
        my @report = split m/\s/sxm, $line;
        if ( is_safe_report(@report) ) {
            $safe_reports++;
        }
    }

    return $safe_reports;
}

1;
