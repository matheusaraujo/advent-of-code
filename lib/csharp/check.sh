#!/bin/bash

year=$1
day=$2

# Create a new console project
dotnet new console -n check -o $year/day$day --force --verbosity quiet

# Add Roslyn analyzer package
dotnet add $year/day$day/check.csproj package Microsoft.CodeAnalysis.NetAnalyzers

# Use sed to add the property inside the PropertyGroup
sed -i '/<\/PropertyGroup>/i \
  <TreatWarningsAsErrors>true</TreatWarningsAsErrors>' $year/day$day/check.csproj

# Build the project
dotnet build $year/day$day/check.csproj --verbosity quiet


