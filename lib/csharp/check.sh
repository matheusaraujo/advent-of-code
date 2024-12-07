#!/bin/bash

year=$1
day=$2

dotnet new console -n check -o $year/day$day --force --verbosity quiet

dotnet add $year/day$day/check.csproj package Microsoft.CodeAnalysis.NetAnalyzers

sed -i '/<\/PropertyGroup>/i \
  <TreatWarningsAsErrors>true</TreatWarningsAsErrors>' $year/day$day/check.csproj

dotnet build $year/day$day/check.csproj --verbosity quiet


