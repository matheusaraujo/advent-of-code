use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;
    my $safe_reports = 0;

    foreach my $line (@puzzle_input) {
        my @report = split m/\s/sxm, $line;
        if ( is_safe_report(@report) ) {
            $safe_reports++;
        }
        else {
            for my $i ( 0 .. $#report ) {
                my @left_report = $i > 0 ? @report[ 0 .. $i - 1 ] : ();
                my @right_report =
                  $i < $#report ? @report[ $i + 1 .. $#report ] : ();

                if ( is_safe_report( @left_report, @right_report ) ) {
                    $safe_reports++;
                    last;
                }
            }
        }
    }

    return $safe_reports;
}

1;

