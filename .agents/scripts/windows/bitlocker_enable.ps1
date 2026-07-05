$drive = 'C:'
$status = Get-BitLockerVolume -MountPoint $drive
if ($status.VolumeStatus -eq 'FullyDecrypted') {
  Enable-BitLocker -MountPoint $drive -EncryptionMethod Aes256 -TPMAndPinProtector -TpmAndPinProtector
  'BITLOCKER_ENABLED'
} else {
  'BITLOCKER_ALREADY_ON'
}
