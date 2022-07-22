package edu.uci.iotproject.analysis;

import java.time.Instant;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;

/**
 * Models a user's action, such as toggling the smart plug on/off at a given time.
 *
 * @author Janus Varmarken
 */
public class UserAction {

    private static volatile DateTimeFormatter TIMESTAMP_FORMATTER = DateTimeFormatter.ISO_ZONED_DATE_TIME.
            withZone(ZoneId.of("America/Los_Angeles"));

    /**
     * Sets the {@link DateTimeFormatter} used when outputting a user action as a string and parsing a user action from
     * a string.
     * @param formatter The formatter to use for outputting and parsing.
     */
    public static void setTimestampFormatter(DateTimeFormatter formatter) {
        TIMESTAMP_FORMATTER = formatter;
    }

    /**
     * Instantiates a {@code UserAction} from a string that obeys the format used in {@link UserAction#toString()}.
     * @param string The string that represents a {@code UserAction}
     * @return A {@code UserAction} resulting from deserializing the string.
     */
    public static UserAction fromString(String string) {
        String[] parts = string.split("@");
        if (parts.length != 2) {
            throw new IllegalArgumentException("Invalid string format");
        }
        // If any of these two parses fail, an exception is thrown -- no need to check return values.
        UserAction.Type actionType = UserAction.Type.valueOf(parts[0].trim());
        Instant timestamp = TIMESTAMP_FORMATTER.parse(parts[1].trim(), Instant::from);
        return new UserAction(actionType, timestamp);
    }


    /**
     * The specific type of action the user performed.
     */
    private final Type mType;

    /**
     * The time the action took place.
     */
    private final Instant mTimestamp;

    public UserAction(Type typeOfAction, Instant timeOfAction) {
        mType = typeOfAction;
        mTimestamp = timeOfAction;
    }

    /**
     * Get the specific type of action performed by the user.
     * @return the specific type of action performed by the user.
     */
    public Type getType() {
        return mType;
    }

    /**
     * Get the time at which the user performed this action.
     * @return the time at which the user performed this action.
     */
    public Instant getTimestamp() {
        return mTimestamp;
    }

    /**
     * Enum for indicating what type of action the user performed.
     */
    public enum Type {
        TOGGLE_ON, TOGGLE_OFF
    }


    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj instanceof UserAction) {
            UserAction that = (UserAction) obj;
            return this.mType == that.mType && this.mTimestamp.equals(that.mTimestamp);
        } else {
            return false;
        }
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int hashCode = 17;
        hashCode = prime * hashCode + mType.hashCode();
        hashCode = prime * hashCode + mTimestamp.hashCode();
        return hashCode;
    }

    @Override
    public String toString() {
       return String.format("%s @ %s", mType.name(), TIMESTAMP_FORMATTER.format(mTimestamp));
    }
}
