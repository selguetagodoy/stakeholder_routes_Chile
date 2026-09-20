# Monitoring methodology

## Separation from the structural model

The institutional and route datasets describe relatively stable structures. The monitoring layer describes volatile facts: current officeholders, open consultations and regulatory dates. These datasets are therefore maintained separately.

## Current authorities

Every row is backed by an official institutional source and carries `last_verified`. A blank `valid_from` means the current officeholder was verified but an exact start date was not established from the selected source. `appointment_status` distinguishes titular from acting/subrogante appointments.

The dataset is descriptive. It does not rank political influence, access, ideology, importance or stakeholder priority.

## Consultations

`status_as_of` is valid only for the snapshot date. If an official source gives an opening date plus a duration rather than a closing date, the calculated closing date is permitted only when `close_date_basis` explicitly records the derivation.

## Regulatory calendar

Exact legal or institutional dates are preferred. Month-level dates remain month-level; the dataset does not invent a day. Mechanically derived deadlines are identified as derived, not official quoted dates.

## Deferred legislation

A future legal regime is not modeled as currently effective. Law N°21.719 is therefore shown as a future milestone for 2026-12-01 rather than as an operative current personal-data route in the 2026-09-19 snapshot.
